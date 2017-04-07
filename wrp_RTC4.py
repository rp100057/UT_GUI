
"""
provides interfaces to the Scanlab RTC card and Aerotech A3200 Axes

"""

from __future__ import division

import ctypes



class wrp_RTC4:
    """
    This class provides interfaces to the Scanlab RTC4 card

    It has 'private' members for the DLL fucntions and accessable functions for use in other programs and classes

    Attributes:
        dll_path = the path to the RTC4DLL.dll file
        dll_initialized = True when the DLL is initialized otherwise False
    """
    def __init__(self): #takes as input the gate time wondow for a single pulse in microseconds
        self.PulseTimeWindow=2300 #each unit is 10mus for example (9 means 90mus)
        return
    
    
    def InitCard(self):

        """
        Initalizes the class and set all python variables to their defaults

        """

        self.rtc_dll = ctypes.WinDLL('C:\RTC4\RTC4DLL.dll')
        self.rtc_dll.load_program_file('C:\RTC4\RTC4D2.hex')
        self.rtc_dll.set_laser_mode(4)
        self.rtc_dll.set_standby(800,8)
        
        #Timing, delay and speed preset
        self.rtc_dll.set_start_list(1)
        self.rtc_dll.set_laser_timing(100,50,50,0)
        self.rtc_dll.set_scanner_delays(25,10,5) 
        self.rtc_dll.set_laser_delays(100,0)
        #self.rtc_dll.set_jump_speed(10)
        #self.rtc_dll.set_mark_speed(250)
        self.rtc_dll.set_end_of_list()
        self.rtc_dll.execute_list(1)
    
    def LaserOn(self):
        self.rtc_dll.laser_signal_on()
        
    def LaserOff(self):
        self.rtc_dll.laser_signal_off()
        
    
    def UpdateLaserPower(self,power_percentage):
        if power_percentage>=0 and power_percentage<=100 :
            tenbitsvalue=(power_percentage/100.0)*1023
            tenbitsvalue=int(tenbitsvalue)
            self.rtc_dll.write_da_2(tenbitsvalue)
        else:
            print "Percentage inserted is not correct"
    
    def ReleaseSinglePulse(self):
        self.rtc_dll.set_start_list(1)
        self.rtc_dll.laser_signal_on_list()
        self.rtc_dll.long_delay(self.PulseTimeWindow) 
        self.rtc_dll.laser_signal_off_list()
        self.rtc_dll.set_end_of_list()
        self.rtc_dll.execute_list(1)
        
    def ReleaseMultiplePulses(self, NumberOfPulses):
        self.rtc_dll.set_start_list(1)
        self.rtc_dll.laser_signal_on_list()
        
        delaysnumber=int(NumberOfPulses*self.PulseTimeWindow/65500)
        """
        The long_delay function takes at most 65500 (time) bits as input.
        Each bit corresponds to 10mus.
        If the number of pulses * pulse time window is greater than the 65500 limit, it is needed to have more long_delay(s). 
        """
        
        if (NumberOfPulses*self.PulseTimeWindow)<65500:       
            self.rtc_dll.long_delay(self.PulseTimeWindow*NumberOfPulses)

            
        else:
            for index in range(delaysnumber):
                self.rtc_dll.long_delay(65500)
            RemainingTimeBits=(NumberOfPulses*self.PulseTimeWindow)-(delaysnumber*65500)
            self.rtc_dll.long_delay(RemainingTimeBits) 
             
        self.rtc_dll.laser_signal_off_list()
        self.rtc_dll.set_end_of_list()
        self.rtc_dll.execute_list(1)
        
                


