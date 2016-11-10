# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 19:32:15 2016

@author: Ralph
"""

import sys
import time
import Queue
import threading
from PyQt4 import QtGui

import lift_gui
import ctrl_generic
import global_parameters

class MainApp(QtGui.QMainWindow, lift_gui.Ui_MainWindow):
    def __init__(self,q1,q2):
        super(self.__class__, self).__init__()
        self.setupUi(self)  

        self.active=False
        self.receiver_q=Queue.Queue()
        self.receiver_q=q1
        self.status_q=Queue.Queue()
        self.status_q=q2
        self.status_t=threading.Thread(target=self.status_loop)
        self.update_options = {
                                'update_receiver_x' : self.update_receiver_x,
                                'update_receiver_y' : self.update_receiver_y,
                                'update_receiver_z' : self.update_receiver_z,
                                }

#        self.actionClose.triggered.connect(self.close)
        self.pushButton_receiver_stepper_x_move_abs.clicked.connect(self.receiver_move_x)

    def status_loop(self):
        while self.active==True:
#            print 'status active'
            time.sleep(0.1)

            if not self.status_q.empty():        
                item=self.status_q.get()
                self.update_options[item[0]](item[1])
                self.status_q.task_done()
        
    def run(self):
        self.active=True
        self.status_t.start()

    def stop(self):
        self.active=False
        self.status_t.join()

    def receiver_move_x(self):
        print("Command sent")
        self.receiver_q.put(['move_abs_x',777],False)
        
    def update_receiver_x(self,pos):
        self.lcdNumber_receiver_stepper_x.display(pos) 
        global gbl_receiver_x_pos
        gbl_receiver_x_pos=pos
               
    def update_receiver_y(self,pos):     
        global gbl_receiver_y_pos
        gbl_receiver_y_pos=pos
        
    def update_receiver_z(self,pos):
        global gbl_receiver_z_pos
        gbl_receiver_z_pos=pos
        

def main():
    receiver_q = Queue.Queue()
    status_q = Queue.Queue()
    ctl=ctrl_generic.control(receiver_q,status_q)
    ctl.run()
    
    app = QtGui.QApplication(sys.argv)  
    form = MainApp(receiver_q,status_q)
    form.run()
    form.show()                         
    app.exec_()
    form.stop()
    print gbl_receiver_x_pos
    
    time.sleep(1)
    ctl.stop()


if __name__ == '__main__':              
    main()  
