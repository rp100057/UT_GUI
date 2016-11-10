import time
import threading
import Queue

class control:
    def __init__(self,q1,q2):
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
                        'move_abs_y' : self.move_abs_z,
                        'move_rel_x' : self.move_rel_x,
                        'move_rel_y' : self.move_rel_y,
                        'move_rel_y' : self.move_rel_z,
                        'home_x' : self.home_x,
                        'home_y' : self.home_y,
                        'home_y' : self.home_z,
                       }

    def worker_loop(self):
        while self.active==True:
#            print 'worker active'
            time.sleep(1)

            if not self.worker_q.empty():        
                item=self.worker_q.get();
                self.worker_options[item[0]](item[1])
                self.worker_q.task_done()

    def sender_loop(self): 
        while self.active==True:
#            print 'sender active'
            time.sleep(1)
            self.sender_q.put(['update_receiver_x',self.get_pos_x()],False)
            self.sender_q.put(['update_receiver_y',self.get_pos_y()],False)
            self.sender_q.put(['update_receiver_z',self.get_pos_z()],False)
        
                
    def run(self):
         self.active=True
         self.worker_t.start()
         self.sender_t.start()
    
    def stop(self):
        self.active=False
        self.worker_t.join()
        self.sender_t.join()     
        
    def home_x(self):
        print 'Home x'

    def home_y(self):
        print 'Home y'
        
    def home_z(self):
        print 'Home z'
        
    def move_abs_x(self,pos):
        print "Moved abs x to "+str(pos)

    def move_abs_y(self,pos):
        print "Moved abs y to "+str(pos)
        
    def move_abs_z(self,pos):
        print "Moved abs z to "+str(pos)

    def move_rel_x(self,delta):
        print "Relative move x of "+str(delta)

    def move_rel_y(self,delta):
        print "Relative move y of "+str(delta)  
        
    def move_rel_z(self,delta):
        print "Relative move z of "+str(delta)  
        
    def get_pos_x(self):
#        print 'Get pos x'
        return 42
        
    def get_pos_y(self):
#        print 'Get pos y'
        return 21
        
    def get_pos_z(self):
#        print 'Get pos z'
        return 84