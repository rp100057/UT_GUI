# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 14:36:45 2016

@author: rpo
"""
from ctypes import *
import time

	
class wrp_thorlabs_sbcStepper:
    def __init__(self,serial):
        self.sbcStepper = cdll.LoadLibrary("Thorlabs//Thorlabs.MotionControl.Benchtop.StepperMotor.dll")
        self.sn = serial #"70866729";
        self.channel=c_short(1);
        self.dt=c_int(200);
#        self.busy = 0;
        self.status=0;
        self.posConv = 819200.0 #digits/mm
#        self.velConv = 766618 # 766618 digits/mm/s
#        self.accConv = 261 # 261 digits/mm/s/s
#        self.pos = 6 #mm
#        self.vel = 2 #mm/s
#        self.acc = 1 #mm/s/s
    
    def wait_axis(self):
        try:       
            self.status=0
        except:
            print "Error occured during \"wait_axis\"!"
        return    
    
    def init_axis(self):
        try:
            self.sbcStepper.TLI_BuildDeviceList()
            self.sbcStepper.SBC_Open(self.sn)
            self.sbcStepper.SBC_LoadSettings(self.sn,self.channel)
            self.sbcStepper.SBC_StartPolling(self.sn,self.channel,self.dt)  
        except:
            print "Error occured during \"init_axis\"!"
        return self.status
    
    def close_axis(self):    
        try:
            self.sbcStepper.SBC_StopPolling(self.sn,self.channel)
            self.status=self.sbcStepper.SBC_Close(self.sn)
        except:
            print "Error occured during \"close_axis\"!"
        return self.status
        
    def home_axis(self):
        try:
            self.status=self.sbcStepper.SBC_Home(self.sn,self.channel)
        except:
            print "Error occured during \"home_axis\"!"
        return self.status
        
    def move_abs(self,x):
        try:
            pos=int(x*self.posConv)
            self.sbcStepper.SBC_MoveToPosition(self.sn,self.channel,pos)
        except:
            print "Error occured during \"move_axisAbs\"!"
        return   
        
    def move_rel(self,x):
        try:
            pos=int(x*self.posConv)
            self.sbcStepper.SBC_MoveRelative(self.sn,self.channel,pos)
        except:
            print "Error occured during \"move_axisRel\"!"
    
        return 

    def get_pos(self):
        try:
            temp=self.sbcStepper.SBC_GetPosition(self.sn,self.channel)/self.posConv
        except:
            print "Error occured during \"move_axisRel\"!"
    
        return temp
    
