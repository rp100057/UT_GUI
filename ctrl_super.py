# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 10:23:13 2017

@author: rpo
"""

import time
import threading
import Queue
import global_parameter as gb

from scipy import misc
from termcolor import colored
import scipy.io

class ctrl_super:
    def __init__(self,q1,q2,q3,q4,q5,q6):
        self.worker_q=Queue.Queue()
        self.worker_q=q1
        self.sender_q=Queue.Queue()
        self.sender_q=q2
        self.donor_q=Queue.Queue()
        self.donor_q=q3
        self.receiver_q=Queue.Queue()
        self.receiver_q=q4
        self.zstage_q=Queue.Queue()
        self.zstage_q=q5
        self.laser_q=Queue.Queue()
        self.laser_q=q6
        self.active=False
        self.worker_t=threading.Thread(target=self.worker_loop)
        
        self.worker_options = {
                        'print3D' : self.print3D
                       }
        self.direction=1
        self.condition = { 1 : gb.gbl_donor_x_refresh_bound,
                          -1 : 0
                          }
        self.pause=False
        
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

    #release single laser pulse with specific power setting
    def release_laser(self):
        print colored('Fire Laser','red')
        self.laser_q.put(['single_pulse',0],False) 
        return True

    # refresh in a simple array like mannor; keep track of used areas
    def refresh_donor(self):
        print 'Refresh Donor'
                
        if(self.direction*gb.gbl_donor_x_pos <= self.condition[self.direction]):
            self.donor_q.put(['move_rel_x',self.direction*gb.gbl_donor_refresh_distance],False)

        else:
            self.donor_q.put(['move_rel_y',gb.gbl_donor_refresh_distance],False)
            self.direction=-1*self.direction
#        time.sleep(1)    
        
        
    #move receiver to correct coordinate; dont move each step, only to the position of the next print dot
    def move_receiver(self,x,y):
        print '=== Move Receiver to ==='
        print x*self.Receiver_dx,y*self.Receiver_dy
        self.receiver_q.put(['move_abs_x',x*self.Receiver_dx],False)
        self.receiver_q.put(['move_abs_y',y*self.Receiver_dy],False)
#        time.sleep(1)
        return True

    #layer finished, move to new layer
    def new_layer(self):
        print '=== New Layer ==='
        self.receiver_q.put(['move_rel_z',self.Receiver_dz],False)
        return True
        
    def read_specs(self):
        #load parameters
        self.mat = scipy.io.loadmat('C:\\Users\\Administrator\\Desktop\\UT_GUI\\printing_test\\specs.mat') 
        self.Receiver_dx=self.mat['print_displacement'][0,0]*1e3 #step from pixel to pixel in x [mm]
        self.Receiver_dy=self.mat['print_displacement'][0,0]*1e3 #step from pixel to pixel in y [mm]
        self.Receiver_dz=-1.0*self.mat['layer_displacement'][0,0]*1e3 #step from layer to layer in z [mm]
        self.steps_z=range(1,self.mat['layers'][0,0]+1)
#        self.steps_z=range(1,3)
        
    def print3D(self,dummy):
        print "Starting routine to print 3D part from slices"
        
        print "Read specifications"
        self.read_specs()
        #load txt file that contains pixel size etc.
        print "Move to initial conditions and set laser power"
        self.laser_q.put(['update_laser_power',dummy],False)        
        
        print "Print slices"
        for k in self.steps_z:
            print k
            layer_data = misc.imread('C:\\Users\\Administrator\\Desktop\\UT_GUI\\printing_test\\array'+str(k)+'.png','L')
            [steps_x,steps_y]=layer_data.shape
            
            for i in range(0,steps_x):
                for j in range(0,steps_y):
                    if layer_data[i,j]:
                        t=time.clock()
                        self.move_receiver(i,j)
                        time.sleep(0.5) # to be adjusted
                        self.release_laser()
                        self.refresh_donor()                  
                        print 'time needed: ' + str(time.clock()-t)
                        while self.pause:
                            time.sleep(0.1)
                        
            self.new_layer()

    def energy(self,dummy):
        print "Starting Energy Scan"
        
        
        #load txt file that contains pixel size etc.
        print "Move to initial conditions and set laser power"
        energy_min=0
        energy_max=100
        delta=10
        
        spatial=0.05 #mm
        steps_per_energy=5
        print "Print slices"
        
        for i in range(energy_min,energy_max+delta,delta):
            self.laser_q.put(['update_laser_power',i],False) 
            
            for j in range(0,steps_per_energy):
                self.release_laser()
                self.receiver_q.put(['move_rel_x',spatial],False)
                self.refresh_donor()
                
            self.receiver_q.put(['move_rel_y',spatial],False)

                        
