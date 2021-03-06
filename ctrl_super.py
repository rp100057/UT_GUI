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
                        'print3D_multi' : self.print3D_multi,
                        'energy' : self.energy,
                        'focus' : self.focus,
                       }
        self.direction_A=1
        
                           
                       
        self.direction_B=1
        self.condition_B = { 1 : gb.gbl_dict['gbl_donor_x_refresh_bound_B_up'],
                            -1 : gb.gbl_dict['gbl_donor_x_refresh_bound_B_down']
                           }
        
        #define start locations from current position
        self.donor_pos_A_x_hist = gb.gbl_dict['gbl_donor_x_pos']
        self.donor_pos_A_y_hist = gb.gbl_dict['gbl_donor_y_pos'] 
        self.donor_pos_B_x_hist = gb.gbl_dict['gbl_donor_x_pos']+gb.gbl_dict['gbl_donor_x_refresh_bound_B_down']
        self.donor_pos_B_y_hist = gb.gbl_dict['gbl_donor_y_pos']+gb.gbl_dict['gbl_donor_y_refresh_bound_B_down']        
        
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
            est_time = (self.progress_total-self.progress_current)*gb.gbl_dict['gbl_super_settling_delay']/60.0
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
        time.sleep(gb.gbl_dict['gbl_super_settling_delay']) 
        self.laser_q.put(['single_pulse',0],False) 
        return True

    def refresh_donor(self,dummy='A'):
        self.condition_A = { 1 : gb.gbl_dict['gbl_donor_x_refresh_bound_A_up'],-1 : gb.gbl_dict['gbl_donor_x_refresh_bound_A_down']}
        if dummy == 'A':             
            if(self.direction_A*gb.gbl_dict['gbl_donor_x_pos'] <= self.direction_A*self.condition_A[self.direction_A]):
                self.donor_q.put(['move_rel_x',self.direction_A*gb.gbl_dict['gbl_donor_refresh_distance']],False)
            else:
                self.donor_q.put(['move_rel_y',gb.gbl_dict['gbl_donor_refresh_distance']],False)
                self.direction_A=-1*self.direction_A
                
        if dummy == 'B':             
            if(self.direction_B*gb.gbl_dict['gbl_donor_x_pos'] <= self.condition_B[self.direction_B]):
                self.donor_q.put(['move_rel_x',self.direction_B*gb.gbl_dict['gbl_donor_refresh_distance']],False)
            else:
                self.donor_q.put(['move_rel_y',gb.gbl_dict['gbl_donor_refresh_distance']],False)
                self.direction_B=-1*self.direction_B
           
    def move_receiver(self,x,y):
        self.receiver_q.put(['move_abs_x',x*self.Receiver_dx],False)
        self.receiver_q.put(['move_abs_y',y*self.Receiver_dy],False)
        return True

    def new_layer(self):
        self.receiver_q.put(['move_rel_z',self.Receiver_dz],False)
        return True
        
    def read_specs(self,path):
        #load parameters
        self.mat = scipy.io.loadmat(self.cwd+path+'\\specs.mat') 
        self.Receiver_dx=self.mat['print_displacement'][0,0]*1e3 #step from pixel to pixel in x [mm]
        self.Receiver_dy=self.mat['print_displacement'][0,0]*1e3 #step from pixel to pixel in y [mm]
        self.Receiver_dz=-1.0*self.mat['layer_displacement'][0,0]*1e3 #step from layer to layer in z [mm]
        self.steps_z=range(1,int(self.mat['layers'][0,0])+1)
        self.Receiver_dimension_x = int(self.mat['dimension_x'][0,0])-1
        self.Receiver_dimension_y = int(self.mat['dimension_y'][0,0])-1
        
    def print3D(self,dummy):
#        dummy = [laserPower, Path]
        laser_power = dummy[0]
        path = 'A'
        
        print "==== STARTING: print3D ===="
        gb.gbl_dict['gbl_super_stop'] = False
        self.progress_current=0
        
        print "Move to initial conditions and set laser power"
        self.laser_q.put(['update_laser_power',laser_power],False)
        
        print "Read specifications from file"
        self.read_specs('\\Blueprints\\Material_'+path)        
        self.progress_total = (self.Receiver_dimension_x)*(self.Receiver_dimension_y)*max(self.steps_z)
        
        for k in self.steps_z:
            print "Print slice number: "+str(k)
            layer_data = misc.imread(self.cwd+'\\Blueprints\\Material_'+path+'\\array'+str(k)+'.png','L')
  
            for i in np.arange(0,self.Receiver_dimension_x):                                 
                for j in np.arange(0,self.Receiver_dimension_y):
                    self.progress_current=float(1+j+i*(self.Receiver_dimension_y)+(self.Receiver_dimension_x)*(self.Receiver_dimension_y)*(k-1))                    
                    if gb.gbl_dict['gbl_super_stop']:
                            break                    
                    while gb.gbl_dict['gbl_super_pause']:
                            time.sleep(0.1) 
                    if layer_data[i,j]:
                        self.move_receiver(i,j)
                        self.release_laser()
                        self.refresh_donor(path)                                                                    
                if gb.gbl_dict['gbl_super_stop']:
                    break
            
            if gb.gbl_dict['gbl_super_stop']:
                    break    
            self.new_layer()
        time.sleep(1)
        print '==== SCRIPT FINISHED ===='

    def energy(self,dummy):
        print "==== STARTING: energy scan ===="
        #dummy [min,max,delta,num,spatial]
        gb.gbl_dict['gbl_super_stop'] = False
        self.progress_current=0
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
                self.progress_current = ((i-energy_min)/(delta)*steps_per_energy+j+1)
                
                if gb.gbl_dict['gbl_super_stop']:
                    break
                while gb.gbl_dict['gbl_super_pause']:
                            time.sleep(0.1)
                self.release_laser()
                self.receiver_q.put(['move_rel_x',k*spatial_step],False)
                self.refresh_donor()
            
            if gb.gbl_dict['gbl_super_stop']:
                    break    
            self.receiver_q.put(['move_rel_y',spatial_step],False)
            k=-1*k
        time.sleep(1)
        print '==== SCRIPT FINISHED ===='
        
    def focus(self,dummy):
        print "==== STARTING: focus scan ===="
        #dummy [min,max,delta,laser_power]
        gb.gbl_dict['gbl_super_stop'] = False
        self.progress_current=0
        
        z_min=dummy[0]
        z_max=dummy[1]
        z_delta=dummy[2]
        laser_power=dummy[3]
        steps_per_z=dummy[4]
        spatial_step=dummy[5] #mm
        marking_offset=4
        k=1
        ii=1
        self.laser_q.put(['update_laser_power',laser_power],False)
        self.zstage_q.put(['move_abs_z',z_min],False)
        time.sleep(2)
        
        self.progress_total = ((z_max-z_min)/z_delta+1)*steps_per_z   
        
        for i in np.arange(z_min,z_max+z_delta,z_delta):
            for j in np.arange(0,steps_per_z):
                self.progress_current = ((i-z_min)/z_delta*steps_per_z+j+1)
                if gb.gbl_dict['gbl_super_stop']:
                    break
                while gb.gbl_dict['gbl_super_pause']:
                            time.sleep(0.1)
                self.release_laser()
                self.donor_q.put(['move_rel_x',k*spatial_step],False)
            if gb.gbl_dict['gbl_super_stop']:
                break 
            
            # Add markings to every fith line
            if(ii%5 == 0 and ii > 0):
                print 'ADD MARKING'
                self.donor_q.put(['move_rel_x',marking_offset*k*spatial_step],False)
                
                number_of_markings = int(ii/5)
                for m in range(0,number_of_markings):
                    self.donor_q.put(['move_rel_x',k*spatial_step],False)
                    self.release_laser()
                    print m
                #moving back to line
                self.donor_q.put(['move_rel_x',-1*k*(marking_offset+number_of_markings)*spatial_step],False)
                print 'marking finished'
            ii+=1
            self.donor_q.put(['move_rel_y',spatial_step],False)
            k=-1*k
            self.zstage_q.put(['move_abs_z',i],False)
        time.sleep(1)
        print '==== SCRIPT FINISHED ===='
        
        
    def print3D_multi(self,dummy):
        print "==== STARTING: print3D multi ===="
        gb.gbl_dict['gbl_super_stop'] = False
        self.progress_current=0
        progress_A = 0
        progress_B = 0
        # run print3D on two folders
        laser_power_A=dummy[0]
        laser_power_B=dummy[1]

        self.read_specs('\\Blueprints\\Material_A')
        self.progress_total = (self.Receiver_dimension_x)*(self.Receiver_dimension_y)*(max(self.steps_z)+1)*2
        for k in self.steps_z:
            if gb.gbl_dict['gbl_super_stop']:
                break
            print 'Print slice number: '+str(k)+' from material A' 
            #Material A
            path = 'A'
            #move to old donor pos
            self.donor_q.put(['move_abs_x',self.donor_pos_A_x_hist,],False)
            self.donor_q.put(['move_abs_y',self.donor_pos_A_y_hist,],False)
            
            self.laser_q.put(['update_laser_power',laser_power_A],False)
            self.read_specs('\\Blueprints\\Material_'+path)
            layer_data = misc.imread(self.cwd+'\\Blueprints\\Material_'+path+'\\array'+str(k)+'.png','L')
            for i in np.arange(0,self.Receiver_dimension_x):
                    if gb.gbl_dict['gbl_super_stop']:
                        break                                 
                    for j in np.arange(0,self.Receiver_dimension_y):
                        self.progress_current=progress_B+float(1+j+i*(self.Receiver_dimension_y)+(self.Receiver_dimension_x)*(self.Receiver_dimension_y)*(k-1))
                        if gb.gbl_dict['gbl_super_stop']:
                            break
                        while gb.gbl_dict['gbl_super_pause']:
                            time.sleep(0.1)
                        if layer_data[i,j]:
                            self.move_receiver(i,j)
                            self.release_laser()
                            self.refresh_donor(path)
                            
            time.sleep(0.5)
            progress_A=self.progress_current
            self.donor_pos_A_x_hist = gb.gbl_dict['gbl_donor_x_pos']
            self.donor_pos_A_y_hist = gb.gbl_dict['gbl_donor_y_pos']
            
            print 'Print slice number: '+str(k)+' from material B' 
            path = 'B'
             #move to old donor pos
            self.donor_q.put(['move_abs_x',self.donor_pos_B_x_hist,],False)
            self.donor_q.put(['move_abs_y',self.donor_pos_B_y_hist,],False)
            
            self.laser_q.put(['update_laser_power',laser_power_B],False)
            self.read_specs('\\Blueprints\\Material_'+path)
            layer_data = misc.imread(self.cwd+'\\Blueprints\\Material_'+path+'\\array'+str(k)+'.png','L')
            for i in np.arange(0,self.Receiver_dimension_x):
                    if gb.gbl_dict['gbl_super_stop']:
                        break                                 
                    for j in np.arange(0,self.Receiver_dimension_y):
                        self.progress_current=progress_A+float(1+j+i*(self.Receiver_dimension_y)+(self.Receiver_dimension_x)*(self.Receiver_dimension_y)*(k-1))
                        if gb.gbl_dict['gbl_super_stop']:
                            break
                        while gb.gbl_dict['gbl_super_pause']:
                            time.sleep(0.1)
                        if layer_data[i,j]:
                            self.move_receiver(i,j)
                            self.release_laser()
                            self.refresh_donor(path)
            time.sleep(0.5) 
            progress_B=self.progress_current
            self.donor_pos_B_x_hist = gb.gbl_dict['gbl_donor_x_pos']
            self.donor_pos_B_y_hist = gb.gbl_dict['gbl_donor_y_pos']
            self.new_layer()
        time.sleep(1)    
        print '==== SCRIPT FINISHED ===='
        return 0