# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 14:16:02 2016

@author: rpo
"""
import time

class LIFT_logging:
    def __init__(self):
        self.path='Logging//LIFT_logging.log'
        self.file = open(self.path, 'a')
        self.file.write('=== NEW SESSION STARTED AT: '+str(time.asctime())+' ===\n')
        self.file.close()
        
    def error(self,msg):
        self.file = open(self.path, 'a')
        self.file.write(str(time.asctime())+'\t Error\t\t'+msg+'\n')
        self.file.close()
        
    def warning(self,msg):
        self.file = open(self.path, 'a')
        self.file.write(str(time.asctime())+'\t Warning\t'+msg+'\n')
        self.file.close()
        
    def debug(self,msg):
        self.file = open(self.path, 'a')
        self.file.write(str(time.asctime())+'\t Debug\t\t'+msg+'\n')
        self.file.close()