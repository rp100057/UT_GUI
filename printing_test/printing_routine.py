# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 10:09:09 2017

@author: rpo
"""

from scipy import misc
from termcolor import colored
import scipy.io
    
 
#load parameters
mat = scipy.io.loadmat('C:\\Users\\rpo\\Documents\\GitHub\\UT_GUI\\printing_test\\specs.mat') 
Receiver_dx=mat['print_displacement'][0,0] #step from pixel to pixel in x [m]
Receiver_dy=mat['print_displacement'][0,0] #step from pixel to pixel in y [m]
Receiver_dz=mat['layer_displacement'][0,0] #step from layer to layer in z [m]
steps_z=range(1,mat['layers'][0,0])

DonorCurrentPos_x=0
DonorCurrentPos_y=0
Donor_delta=30e-6
DonorBound_x=5e-3
DonorBound_y=5e-3

#release single laser pulse with specific power setting
def release_laser():
    print colored('Fire Laser','red')
    return True

# refresh in a simple array like mannor; keep track of used areas
def refresh_donor():
    print 'Refresh Donor'
    #move dx*k
    #check bounds; if out of bound change direction(k=-k) and move dy one step further
    
    return True

#move receiver to correct coordinate; dont move each step, only to the position of the next print dot
def move_receiver(x,y):
    print '=== Move Receiver to ==='
    print x*Receiver_dx,y*Receiver_dy
    return True

#layer finished, move to new layer
def new_layer():
    print '=== New Layer ==='
    return True


def read_specs():
    mat = scipy.io.loadmat('C:\\Users\\rpo\\Documents\\GitHub\\UT_GUI\\printing_test\\specs.mat')
    mat['layer_displacement'][0,0]
    mat['print_displacement'][0,0]
    mat['layers'][0,0]
    
    
for k in steps_z:
    print k
    layer_data = misc.imread('array'+str(k)+'.png')
    [steps_x,steps_y]=layer_data.shape    
    
    for i in range(1,steps_x):
        for j in range(1,steps_y):
            if(layer_data[i,j]):
                move_receiver(i,j)
                release_laser()
                refresh_donor()
                
    new_layer()