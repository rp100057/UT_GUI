# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 10:23:13 2017

@author: rpo
"""

import time
import threading
import Queue
import global_parameter as gb
import numpy as np

from scipy import misc
#from termcolor import colored
import scipy.io
import os

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
        self.sender_t=threading.Thread(target=self.sender_loop)
        self.cwd = os.getcwd()        
        self.progress_current = 1.0
        self.progress_total = 1.0       
        
        self.worker_options = {
                        'print3D' : self.print3D,
                        'energy' : self.energy,
                        'focus' : self.focus,
                       }
        self.direction_A=1
        self.condition_A = { 1 : gb.gbl_donor_x_refresh_bound_A,
                          -1 : 0
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
            time.sleep(0.5)
            perc= self.progress_current/self.progress_total*100.0
            est_time = (self.progress_total-self.progress_current)*gb.gbl_super_settling_delay/60.0
            arg=[perc,est_time]
            self.sender_q.put(['update_super',arg],False)    
            
    def run(self):
         self.active=True
         self.worker_t.start()
         self.sender_t.start()

    def stop(self):
        self.active=False
        self.worker_t.join()
        self.sender_t.join()
        
    def release_laser(self):
        time.sleep(gb.gbl_super_settling_delay) 
        self.laser_q.put(['single_pulse',0],False) 
        return True

    def refresh_donor(self):             
        if(self.direction_A*gb.gbl_donor_x_pos <= self.condition_A[self.direction_A]):
            self.donor_q.put(['move_rel_x',self.direction_A*gb.gbl_donor_refresh_distance],False)

        else:
            self.donor_q.put(['move_rel_y',gb.gbl_donor_refresh_distance],False)
            self.direction_A=-1*self.direction_A
           
    def move_receiver(self,x,y):
#        print '=== Move Receiver to ==='
#        print x*self.Receiver_dx,y*self.Receiver_dy
        self.receiver_q.put(['move_abs_x',x*self.Receiver_dx],False)
        self.receiver_q.put(['move_abs_y',y*self.Receiver_dy],False)
#        time.sleep(1)
        return True

    def new_layer(self):
#        print '=== New Layer ==='
        self.receiver_q.put(['move_rel_z',self.Receiver_dz],False)
        return True
        
    def read_specs(self,path):
        #load parameters
        self.mat = scipy.io.loadmat(self.cwd+path+'specs.mat') 
        self.Receiver_dx=self.mat['print_displacement'][0,0]*1e3 #step from pixel to pixel in x [mm]
        self.Receiver_dy=self.mat['print_displacement'][0,0]*1e3 #step from pixel to pixel in y [mm]
        self.Receiver_dz=-1.0*self.mat['layer_displacement'][0,0]*1e3 #step from layer to layer in z [mm]
        self.steps_z=range(1,int(self.mat['layers'][0,0])+1)
        self.Receiver_dimension_x = int(self.mat['dimension_x'][0,0])-1
        self.Receiver_dimension_y = int(self.mat['dimension_y'][0,0])-1
        
    def print3D(self,dummy):
#        dummy = [laserPower, Path]
        laser_power = dummy[0]
        path = dummy[1]
        
        print "==== STARTING: print3D ===="
        gb.gbl_super_stop = False
        
        print "Move to initial conditions and set laser power"
        self.laser_q.put(['update_laser_power',laser_power],False)
        
        print "Read specifications from file"
        self.read_specs(path)
#        layer_data = misc.imread(self.cwd+path+'array'+str(1)+'.png','L')
#        [steps_x,steps_y]=layer_data.shape        
        self.progress_total = (self.Receiver_dimension_x)*(self.Receiver_dimension_y)*max(self.steps_z)
        
        for k in self.steps_z:
            print "Print slice number: "+str(k)
            layer_data = misc.imread(self.cwd+path+'array'+str(k)+'.png','L')
#            [self.Receiver_dimension_x,self.Receiver_dimension_y]=layer_data.shape
            
            for i in np.arange(0,self.Receiver_dimension_x):                                 
                for j in np.arange(0,self.Receiver_dimension_y):
                    self.progress_current=float(1+j+i*(self.Receiver_dimension_y)+(self.Receiver_dimension_x)*(self.Receiver_dimension_y)*(k-1))                    
                    if gb.gbl_super_stop:
                            break                    
                    while gb.gbl_super_pause:
                            time.sleep(0.1)                     
                    if layer_data[i,j]:
#                        t=time.clock()
                        self.move_receiver(i,j)
                        self.release_laser()
                        self.refresh_donor()                  
#                        print 'time needed: ' + str(time.clock()-t)                                                   
                if gb.gbl_super_stop:
                    break
            
            if gb.gbl_super_stop:
                    break    
            self.new_layer()
        print '==== SCRIPT FINISHED ===='

    def energy(self,dummy):
        print "==== STARTING: energy scan ===="
        #dummy [min,max,delta,num,spatial]
        gb.gbl_super_stop = False
        energy_min=dummy[0]
        energy_max=dummy[1]
        delta=dummy[2] 
        steps_per_energy=dummy[3] 
        spatial_step=dummy[4]  #mm
        k=1
        self.progress_total = ((energy_max-energy_min)/delta+1)*steps_per_energy      
        
        for i in np.arange(energy_min,energy_max+delta,delta):
            self.laser_q.put(['update_laser_power',i],False)      
            for j in np.arange(0,steps_per_energy):
                self.progress_current = (i/delta*steps_per_energy+j+1)
                
                if gb.gbl_super_stop:
                    break
                while gb.gbl_super_pause:
                            time.sleep(0.1)
                self.release_laser()
                self.receiver_q.put(['move_rel_x',k*spatial_step],False)
                self.refresh_donor()
            
            if gb.gbl_super_stop:
                    break    
            self.receiver_q.put(['move_rel_y',spatial_step],False)
            k=-1*k
        print '==== SCRIPT FINISHED ===='
        
    def focus(self,dummy):
        print "==== STARTING: focus scan ===="
        #dummy [min,max,delta,laser_power]
        gb.gbl_super_stop = False
        z_min=dummy[0]
        z_max=dummy[1]
        z_delta=dummy[2]
        laser_power=dummy[3]
        steps_per_z=dummy[4]
        spatial_step=dummy[5] #mm
        marking_offset=4
        k=1
        self.laser_q.put(['update_laser_power',laser_power],False)
        
        self.progress_total = ((z_max-z_min)/z_delta+1)*steps_per_z   
        
        for i in np.arange(z_min,z_max+z_delta,z_delta):
            for j in np.arange(0,steps_per_z):
                self.progress_current = (i/z_delta*steps_per_z+j+1)
                if gb.gbl_super_stop:
                    break
                while gb.gbl_super_pause:
                            time.sleep(0.1)
                self.release_laser()
                self.donor_q.put(['move_rel_x',k*spatial_step],False)
            if gb.gbl_super_stop:
                break 
            
            # Add markings to every fith line
            if(i%5 == 0 and i > 0): 
                self.donor_q.put(['move_rel_x',marking_offset*k*spatial_step],False)  
                number_of_markings = int(i/5)
                for m in range(0,number_of_markings):
                    self.donor_q.put(['move_rel_x',k*spatial_step],False)                   
                    self.release_laser()
                #moving back to line
                self.donor_q.put(['move_rel_x',-1*(marking_offset+number_of_markings)*k*spatial_step],False)   
            
            self.donor_q.put(['move_rel_y',spatial_step],False)
            k=-1*k
            self.zstage_q.put(['move_abs_z',i],False)
        print '==== SCRIPT FINISHED ===='
        
        
    def print3D_multi(self,dummy):
        # run print3D on two folders
        
        
        return 0