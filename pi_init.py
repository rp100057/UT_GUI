# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 10:52:55 2017

@author: Luigi Capuano
"""

from pipython import GCSDevice, GCSError, gcserror
from time import sleep, time
from logging import debug

"""
Functions taken from the original package necessary for running the startup function
"""

class FrozenClass(object):  # Too few public methods pylint: disable=R0903
    """Freeze child class when self.__isfrozen is set, i.e. values of already existing properties can still
    be changed but no new properties can be added.
    """
    __isfrozen = False

    def __setattr__(self, key, value):
        if self.__isfrozen and key not in dir(self):  # don't use hasattr(), it returns False on any exception
            raise TypeError('%r is immutable, cannot add %r' % (self, key))
        object.__setattr__(self, key, value)

    def _freeze(self):
        """After this method has been called the child class denies adding new properties."""
        self.__isfrozen = True


class GCSRaise(object):  # Too few public methods pylint: disable=R0903
    """Context manager that asserts raising of specific GCSError(s).
    @param gcserrorid : GCSError ID or iterable of IDs that are expected to be raised as integer.
    @param mustraise : If True an exception must be raised, if False an exception can be raised.
    """

    def __init__(self, gcserrorid, mustraise=True):
        self.__expected = gcserrorid if hasattr(gcserrorid, '__iter__') else [gcserrorid]
        self.__mustraise = mustraise and gcserrorid

    def __enter__(self):
        return self

    def __exit__(self, exctype, excvalue, _exctraceback):

        gcsmsg = '%r' % gcserror.translate_error(excvalue)
        if exctype == GCSError:
            if excvalue in self.__expected:
                debug('expected GCSError %s was raised', gcsmsg)
                return True  # do not re-raise
        if not self.__mustraise and excvalue is None:
            debug('no error was raised')
            return True  # do not re-raise
        expected = ', '.join([gcserror.translate_error(errval) for errval in self.__expected])
        msg = 'expected %r but raised was %s' % (expected, gcsmsg)
        raise ValueError(msg)
def stopall(pidevice):
    """Stop motion of all axes and mask the "error 10" warning.
    @type pidevice : pipython.gcscommands.GCSCommands
    """
    try:
        pidevice.StopAll()
    except GCSError as exc:
        if gcserror.E10_PI_CNTR_STOP != exc:  # error 10 is just a warning that the device has been stopped
            raise
            
def getaxeslist(pidevice, axes):
    """Return list of 'axes'.
    @type pidevice : pipython.gcscommands.GCSCommands
    @param axes : Axis as string or list of them or None for all axes.
    @return : List of axes from 'axes' or all axes or empty list.
    """
    axes = pidevice.axes if axes is None else axes
    if not axes:
        return []
    if not hasattr(axes, '__iter__'):
        axes = [axes]
    return axes

def waitonready(pidevice, timeout=60):
    """Wait until controller is on "ready" state.
    @type pidevice : pipython.gcscommands.GCSCommands
    @param timeout : Timeout in seconds, defaults to 60 seconds.
    """
    if not pidevice.HasIsControllerReady():
        return
    maxtime = time() + timeout
    while not pidevice.IsControllerReady():
        if time() > maxtime:
            raise SystemError('waitonready() timed out after %.1f seconds' % timeout)
        sleep(0.1)

def waitontarget(pidevice, axes=None, timeout=60):
    """Wait until all 'axes' are on target.
    @type pidevice : pipython.gcscommands.GCSCommands
    @param axes : Axes to wait for as string or list, or None to wait for all axes.
    @param timeout : Timeout in seconds as float, defaults to 60 seconds.
    """
    axes = getaxeslist(pidevice, axes)
    if not axes:
        return
    waitonready(pidevice, timeout)
    maxtime = time() + timeout
    while not all(list(pidevice.qONT(axes).values())):
        if time() > maxtime:
            raise SystemError('waitontarget() timed out after %.1f seconds' % timeout)
        sleep(0.1)
        


"""
Startup function: initialize the stages in two main steps:
1) uploads the parameter file on the controller
2)references the axis by going to known position (i.e. Negative or positive limit or reference switch)
"""

def startup(CONTROLLERNAME, STAGES, REFMODE): 
    
    """
    Examples of inputs:
    CONTROLLERNAME = 'Hydra' string, select the right DLL to use with the controller
    STAGES = ('UPS-150','NOSTAGE')  list, assign the stage types to axes
    REFMODE = ('FNL', None)  list, reference the connected stages (can be FNL, FPL, FRF)
    
    If you want to skip something use None as value
    """
    
    # 1. Initialization of the axes
    
    with GCSDevice(CONTROLLERNAME) as pidevice: #select the right DLL to use with the controller

        pidevice.ConnectRS232(comport=1, baudrate=115200)
        
        
        
        print('connected: {}'.format(pidevice.qIDN().strip()))

        # Shows the version info 

        if pidevice.HasqVER():
           print('version info: {}'.format(pidevice.qVER().strip()))

            
        print 'Initialize connected stages...'
           
           
        """
        in this "if statement" the parameter file of each axis is written in the memory, 
        if the variable STAGES is set to None this part is skipped
        """
        print 'Uploading parameter files...'
        if STAGES:
            allaxes = pidevice.qSAI_ALL()
            stages = STAGES if isinstance(STAGES, (list, tuple)) else [STAGES]
            stages = stages[:len(allaxes)]
            allaxes = allaxes[:len(stages)]
            pidevice.CST(allaxes, stages) 
            sleep(2)
            
        for ax in range (1,len(allaxes)):  
            pidevice.SVO(str(ax), True) #switches all the servos on
            
        stopall(pidevice)
        waitontarget(pidevice, axes=pidevice.axes)
        
        """
        in this "if statement" the axes are referenced using the selected referencing mode
        if the variable REFMODE is set to None this part is skipped
        """        
        print 'Referencing axes...'        
        referencedaxes = []
        if REFMODE:
            refmode = REFMODE if isinstance(REFMODE, (list, tuple)) else [REFMODE] * pidevice.numaxes
            refmode = refmode[:pidevice.numaxes]
            reftypes = set(refmode)
            for reftype in reftypes:
                if reftype is None:
                    continue
                axes = [pidevice.axes[i] for i in range(len(refmode)) if refmode[i] == reftype]
                getattr(pidevice, reftype.upper())(axes)
                
                while pidevice.IsControllerReady()!=True:
                    pidevice.IsControllerReady()
                
                referencedaxes += axes
        waitontarget(pidevice, axes='1')
        
        print 'Homing axes...'
        pidevice.GOH(pidevice.axes) #homes all the axes
        pidevice.close()        
        print('Initialization complete!') 
        





    
