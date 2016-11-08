# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 14:13:12 2016

@author: rpo
"""
import wrp_thorlabs_max3d

class ctrl_receiver:
    
    def __init__(self):
        self.status = 0;
        self.axis = wrp_thorlabs_max3d();
        self.axis.move_abs()
          
    def start(self):
        #start the loop
        self.status = 1;
        
    def stop(self):
        #stop loop
        self.status = 0;
        
        