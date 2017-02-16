import time
import threading
import Queue
import wrp_pistages

class control_donor:
    def __init__(self,q1,q2):
        self.pi_x=wrp_pistages.wrp_pistages(1)
        self.pi_x.init_axis()
#        self.pi_y=wrp_pistages(2)
#        self.pi_y.init_axis()
        self.worker_q=Queue.Queue()
        self.worker_q=q1
        self.sender_q=Queue.Queue()
        self.sender_q=q2
        self.active=False
        self.worker_t=threading.Thread(target=self.worker_loop)
        self.sender_t=threading.Thread(target=self.sender_loop)
        self.worker_options = {
                        'move_abs_x' : self.move_abs_x,
#                        'move_abs_y' : self.move_abs_y,
                        'move_rel_x' : self.move_rel_x,
#                        'move_rel_y' : self.move_rel_y,
                        'home_x' : self.home_x,
#                        'home_y' : self.home_y,
                       }

    def worker_loop(self):
        while self.active==True:
#            print 'worker active'
            time.sleep(0.100)

            if not self.worker_q.empty():        
                item=self.worker_q.get();
                self.worker_options[item[0]](item[1])
                self.worker_q.task_done()

    def sender_loop(self): 
        while self.active==True:
#            print 'sender active'
            time.sleep(0.200)
            self.sender_q.put(['update_donor_x',self.get_pos_x()],False)
#            self.sender_q.put(['update_donor_y',self.get_pos_y()],False)
        
                
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
        self.pi_x.home_axis()
        
#    def home_y(self,dummy):
#        print 'Home y'
#        self.pi_y.home_axis()   
        
    def move_abs_x(self,pos):
        print "Moved abs x to "+str(pos)
        self.pi_x.move_abs(pos)

#    def move_abs_y(self,pos):
#        print "Moved abs y to "+str(pos)
#        self.pi_y.move_abs(pos)

    def move_rel_x(self,delta):
        print "Relative move x of "+str(delta)
        self.pi_x.move_rel(delta)

#    def move_rel_y(self,delta):
#        print "Relative move y of "+str(delta)
#        self.pi_y.move_rel(delta)
        
        
    def get_pos_x(self):
#        print 'Get pos x'
        return self.pi_x.get_pos()
        
#    def get_pos_y(self):
##        print 'Get pos y'
#        return self.pi_y.get_pos()
