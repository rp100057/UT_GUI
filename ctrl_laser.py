import time
import threading
import Queue
import wrp_RTC4
import global_parameter as gb

class control_laser:
    def __init__(self,q1,q2):
        self.laser=wrp_RTC4.wrp_RTC4()
        self.laser.InitCard()
    
        self.worker_q=Queue.Queue()
        self.worker_q=q1
        self.sender_q=Queue.Queue()
        self.sender_q=q2
        self.active=False
        self.worker_t=threading.Thread(target=self.worker_loop)
        self.sender_t=threading.Thread(target=self.sender_loop)
        self.worker_options = {
                        'laser_on' : self.laser_on,
                        'laser_off' : self.laser_off,
                        'update_laser_power' : self.update_laser_power,
                        'single_pulse' : self.single_pulse,
                        'multi_pulse' : self.multi_pulse,             
                       }

    def worker_loop(self):
        while self.active==True:
#            print 'worker active'
            time.sleep(0.01)

            if not self.worker_q.empty():        
                item=self.worker_q.get();
                self.worker_options[item[0]](item[1])
                self.worker_q.task_done()

    def sender_loop(self): 
        while self.active==True:
#            print 'sender active'
            time.sleep(0.100)
            self.sender_q.put(['update_laser',self.get_laser_power()],False)
            self.sender_q.put(['alive_laser',0],False)
        
    def run(self):
         self.active=True
         self.worker_t.start()
         self.sender_t.start()
    
    def stop(self):
        self.active=False
        self.worker_t.join()
        self.sender_t.join()  
                
    def laser_on(self,dummy):
        print 'Laser switched ON'
        self.laser.LaserOn()
    
    def laser_off(self,dummy):
        print 'Laser switched OFF'
        self.laser.LaserOff()
        
    def update_laser_power(self,powerPerc):
        print 'Set laser power to '+str(powerPerc)
        self.laser.UpdateLaserPower(powerPerc)
        gb.gbl_laser_power=powerPerc
        
    def single_pulse(self,dummy):
        print 'Release single pulse'
        self.laser.ReleaseSinglePulse()
        
    def multi_pulse(self,numberOfPulses):
        print 'Release multiple pulses'
        self.laser.ReleaseMultiplePulses(numberOfPulses)
        
    def get_laser_power(self):
        return gb.gbl_laser_power
        
