# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 10:23:13 2017

@author: rpo
"""

import time
import threading
import Queue

class ctrl_super:
    def __init__(self,q1,q2,q3,q4):
        self.worker_q=Queue.Queue()
        self.worker_q=q1
        self.sender_q=Queue.Queue()
        self.sender_q=q2
        self.donor_q=Queue.Queue()
        self.donor_q=q3
        self.receiver_q=Queue.Queue()
        self.receiver_q=q4
        self.active=False
        self.worker_t=threading.Thread(target=self.worker_loop)
        
        self.worker_options = {
                        'print3D' : self.print3D
                       }
        
    def worker_loop(self):
        while self.active==True:
#            print 'worker active'
            time.sleep(0.100)

            if not self.worker_q.empty():        
                item=self.worker_q.get();
                self.worker_options[item[0]](item[1])
                self.worker_q.task_done()
            
    def run(self):
         self.active=True
         self.worker_t.start()

    
    def stop(self):
        self.active=False
        self.worker_t.join()

        
    def print3D(self,dummy):
        print "print something from slices"