import time
import threading
import Queue
import wrp_thorlabs_sbcStepper

class control_receiver:
    def __init__(self,q1,q2):
        self.stepper_x=wrp_thorlabs_sbcStepper.wrp_thorlabs_sbcStepper("70866729",1)
        self.stepper_x.init_axis()
        self.stepper_y=wrp_thorlabs_sbcStepper.wrp_thorlabs_sbcStepper("70866729",2)
        self.stepper_y.init_axis()
        self.stepper_z=wrp_thorlabs_sbcStepper.wrp_thorlabs_sbcStepper("70866729",3)
        self.stepper_z.init_axis()
        self.worker_q=Queue.Queue()
        self.worker_q=q1
        self.sender_q=Queue.Queue()
        self.sender_q=q2
        self.active=False
        self.worker_t=threading.Thread(target=self.worker_loop)
        self.sender_t=threading.Thread(target=self.sender_loop)
        self.worker_options = {
                        'move_abs_x' : self.move_abs_x,
                        'move_abs_y' : self.move_abs_y,
                        'move_abs_z' : self.move_abs_z,
                        'move_rel_x' : self.move_rel_x,
                        'move_rel_y' : self.move_rel_y,
                        'move_rel_z' : self.move_rel_z,
                        'home_x' : self.home_x,
                        'home_y' : self.home_y,
                        'home_z' : self.home_z,
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
            time.sleep(0.1)
            self.sender_q.put(['update_receiver_x',self.get_pos_x()],False)
            self.sender_q.put(['update_receiver_y',self.get_pos_y()],False)
            self.sender_q.put(['update_receiver_z',self.get_pos_z()],False)
            self.sender_q.put(['alive_receiver',0],False)
        
                
    def run(self):
         self.active=True
         self.worker_t.start()
         self.sender_t.start()
    
    def stop(self):
        self.active=False
        self.worker_t.join()
        self.sender_t.join()     
        
    def home_x(self,dummy):
        print 'Home x'
        self.stepper_x.home_axis()
        
    def home_y(self,dummy):
        print 'Home y'
        self.stepper_y.home_axis()
        
    def home_z(self,dummy):
        print 'Home z'
        self.stepper_z.home_axis()
        
        
    def move_abs_x(self,pos):
        print "Moved abs x to "+str(pos)
        self.stepper_x.move_abs(pos)

    def move_abs_y(self,pos):
        print "Moved abs y to "+str(pos)
        self.stepper_y.move_abs(pos)
        
    def move_abs_z(self,pos):
        print "Moved abs z to "+str(pos)
        self.stepper_z.move_abs(pos)

    def move_rel_x(self,delta):
        print "Relative move x of "+str(delta)
        self.stepper_x.move_rel(delta)

    def move_rel_y(self,delta):
        print "Relative move y of "+str(delta)
        self.stepper_y.move_rel(delta)
        
    def move_rel_z(self,delta):
        print "Relative move z of "+str(delta)
        self.stepper_y.move_rel(delta)
        
    def get_pos_x(self):
#        print 'Get pos x'
        return self.stepper_x.get_pos()
        
    def get_pos_y(self):
#        print 'Get pos y'
        return self.stepper_y.get_pos()
        
    def get_pos_z(self):
#        print 'Get pos z'
        return self.stepper_z.get_pos()