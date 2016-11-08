# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 14:36:45 2016

@author: rpo
"""
from ctypes import *
import time

	
class wrp_thorlabs_dcServo:
    def __init__(self):
        self.dcServo = cdll.LoadLibrary("Thorlabs//Thorlabs.MotionControl.TCube.DCServo.dll")
        self.sn = "8123456";
        self.busy = 0;
        self.status=0;
        self.posConv = 34304 #34304 digits/mm
        self.velConv = 766618 # 766618 digits/mm/s
        self.accConv = 261 # 261 digits/mm/s/s
        self.pos = 6 #mm
        self.vel = 2 #mm/s
        self.acc = 1 #mm/s/s
    
    def wait_axis(self):
        try:       
            time.sleep(0.1)
            while self.dcServo.CC_GetStatusBits(self.sn) & 0x00000010 != 0 or self.dcServo.CC_GetStatusBits(sn) & 0x00000020 != 0:        
                print self.dcServo.CC_GetStatusBits(sn) & 0x00000020
                print self.dcServo.CC_GetStatusBits(sn) & 0x00000040
                time.sleep(0.1)
        except:
            print "Error occured during \"wait_axis\"!"
        return    
    
    def init_axis(self):
        try:     
            self.status=self.dcServo.CC_Open(self.sn)
            self.dcServo.CC_StartPolling(self.sn,c_int(50))
            self.dcServo.CC_SetVelParams(self.sn,c_int(int(self.acc*self.accConv)), c_int(int(self.vel*self.velConv)))
        except:
            print "Error occured during \"init_axis\"!"
        return 0
    
    def close_axis(self):    
        try:
            self.dcServo.CC_StopPolling(self.sn)
            self.dcServo.CC_Close(self.sn)        
        except:
            print "Error occured during \"close_axis\"!"
        return
        
    def home_axis(self):
        try:
            self.dcServo.CC_Home(self.sn)
            time.sleep(0.1)
            while self.dcServo.CC_GetStatusBits(self.sn) & 0x00000200 != 0:        
                    print cubeDC.CC_GetStatusBits(self.sn) & 0x00000200
                    time.sleep(0.1)
        except:
            print "Error occured during \"home_axis\"!"
        return
        
    def move_abs(self,x):
        try:
            self.dcServo.CC_MoveToPosition(sn,int(pos*posConv))
            wait_axis(self.sn)
        except:
            print "Error occured during \"move_axisAbs\"!"
        return   
        
    def move_rel(self,dx):
        try:
            self.dcServo.CC_MoveRelative(self.sn, int(dx*self.posConv))
            wait_axis(self.sn)
        except:
            print "Error occured during \"move_axisRel\"!"
    
        return 
    
