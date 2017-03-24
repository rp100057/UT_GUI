import time
import threading
import Queue
import wrp_pistages

class control_zstage:
    def __init__(self,q1,q2):
        self.pi_z=wrp_pistages.wrp_pistages()
        self.pi_z.init_controller('MERCURY')
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
                        'move_abs_z' : self.move_abs_z,
                        'move_rel_z' : self.move_rel_z,
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
            time.sleep(0.100)
            self.sender_q.put(['update_zstage',self.get_pos_z()],False)
            self.sender_q.put(['alive_zstage',0],False)
                      
    def run(self):
         self.active=True
         self.worker_t.start()
         self.sender_t.start()
    
    def stop(self):
        self.active=False
        self.worker_t.join()
        self.sender_t.join()
        self.pi_z.close_axis(3)
    
    def home_z(self,dummy):
        print 'Home z'
        self.pi_z.home_axis(3)   
        
    def move_abs_z(self,pos):
        print "Moved abs z to "+str(pos)
        self.pi_z.move_abs(3,pos)

    def move_rel_z(self,delta):
        print "Relative move z of "+str(delta)
        self.pi_z.move_rel(3,delta)

    def get_pos_z(self):
#        print 'Get pos x'
        return self.pi_z.get_pos(3)['1']
