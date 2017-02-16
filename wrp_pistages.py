# -*- coding: utf-8 -*-
"""
wrp_pistages
Created on Fri Jan 27 11:57:57 2017

@author: CapuanoL
"""
from pi_init import startup, waitontarget
from pipython import GCSDevice


class wrp_pistages:
    """
    A class containing the main functions to use with the PI Stages
    """
       
    def __init__(self,ax):
        self.pixystages=GCSDevice('Hydra') #select the right DLL to use with the controller 
        self.ax=str(ax)
        
        
        return
        
    def wait_axis(self):
       
        return    
    
    def init_axis(self):
        startup('Hydra',('UPS-150','NOSTAGE') ,('FRF', None))
        self.pixystages.ConnectRS232(comport=1, baudrate=115200)

        return 
           
    def home_axis(self):
        self.pixystages.GOH(self.ax)
        
        return
           
    def set_acc(self,acc):
        print 'Acceleration of axis %c set to %f' % (self.ax, acc)
        self.pixystages.ACC(self.ax,acc)
       
        return
   
    def set_vel(self,vel):
        print 'Closed loop velocity of axis %c set to %f' % (self.ax, vel)
        self.pixystages.VEL(self.ax,vel)    

        return
        
    def move_abs(self,x):
        self.pixystages.MOV(self.ax,x)
#        waitontarget(self.pixystages)
#        positions = self.pixystages.qPOS(self.pixystages.axes)     
#        print('Axis {} moved to position {:.4f}'.format(self.ax, positions[self.ax]))
        
        return
                          
    def move_rel(self,dx):
        print 'Relative move axis %c of: %f' % (self.ax, dx)
        self.pixystages.MVR(self.ax,dx)
#        waitontarget(self.pixystages)  
        
        return 
                    
    def close_axis(self):    
        self.pixystages.CloseConnection()
        self.pixystages.unload()
        
        return

    def get_pos(self):
        return self.pixystages.qPOS(self.pixystages.axes)[self.ax]