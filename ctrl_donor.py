import time
import threading
import Queue
import wrp_pistages
import global_parameter as gb

class control_donor:
    def __init__(self,q1,q2):
        self.pi_xy=wrp_pistages.wrp_pistages()
        self.pi_xy.init_controller('Hydra')
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
                        'move_abs_y' : self.move_abs_y,
                        'move_rel_x' : self.move_rel_x,
                        'move_rel_y' : self.move_rel_y,
                        'home_x' : self.home_x,
                        'home_y' : self.home_y,
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
            time.sleep(0.10)
            self.sender_q.put(['update_donor_x',self.get_pos_x()],False)
            self.sender_q.put(['update_donor_y',self.get_pos_y()],False)
            self.sender_q.put(['alive_donor',0],False)
                      
    def run(self):
         self.active=True
         self.worker_t.start()
         self.sender_t.start()
    
    def stop(self):
        self.active=False
        self.worker_t.join()
        self.sender_t.join()
        self.pi_xy.close_axis(1)
        self.pi_xy.close_axis(2)
        
    def home_x(self,dummy):
        print 'Home x'
        self.pi_xy.home_axis(1)
    
    def home_y(self,dummy):
        print 'Home y'
        self.pi_xy.home_axis(2)      
        
    def move_abs_x(self,pos):
        if pos < gb.gbl_donor_x_lim_up and pos >  gb.gbl_donor_x_lim_down:
            print "Moved abs x to "+str(pos)
            self.pi_xy.move_abs(1,pos)
        else:
            print "OUT OF LIMITS"

    def move_abs_y(self,pos):
        if pos < gb.gbl_donor_y_lim_up and pos >  gb.gbl_donor_y_lim_down:
            print "Moved abs y to "+str(pos)
            self.pi_xy.move_abs(2,pos)
        else:
            print "OUT OF LIMITS"

    def move_rel_x(self,delta):
        if gb.gbl_donor_x_pos+delta < gb.gbl_donor_x_lim_up and gb.gbl_donor_x_pos+delta >  gb.gbl_donor_x_lim_down: 
            print "Relative move x of "+str(delta)
            self.pi_xy.move_rel(1,delta)
        else:
            print "OUT OF LIMITS"

    def move_rel_y(self,delta):
        if gb.gbl_donor_y_pos+delta < gb.gbl_donor_y_lim_up and gb.gbl_donor_y_pos+delta >  gb.gbl_donor_y_lim_down: 
            print "Relative move x of "+str(delta)
            self.pi_xy.move_rel(2,delta)
        else:
            print "OUT OF LIMITS"
            
    def get_pos_x(self):
#        print 'Get pos x'
        return self.pi_xy.get_pos(1)
        
    def get_pos_y(self):
#        print 'Get pos x'
        return self.pi_xy.get_pos(2)
