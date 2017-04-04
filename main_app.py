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
from PyQt4 import QtCore

import lift_gui
import ctrl_receiver
import ctrl_donor
import ctrl_zstage
import ctrl_laser
import ctrl_super
import global_parameter as gb

class MainApp(QtGui.QMainWindow, lift_gui.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)  
    
        self.active=False
        self.receiver_q=Queue.Queue()
        self.status_q=Queue.Queue()
        self.donor_q=Queue.Queue()
        self.zstage_q=Queue.Queue()
        self.laser_q=Queue.Queue()
        self.super_q=Queue.Queue()
        self.status_t=threading.Thread(target=self.status_loop)
        self.ctrl_super=ctrl_super.ctrl_super(self.super_q,self.status_q,self.donor_q,self.receiver_q,self.zstage_q,self.laser_q)   
        
        self.status_laser = 999
        self.status_donor = 999
        self.status_receiver = 999
        self.status_zstage = 999
        self.timeout_value = 200
        
        self.update_options = {
                                'update_receiver_x' : self.update_receiver_x,
                                'update_receiver_y' : self.update_receiver_y,
                                'update_receiver_z' : self.update_receiver_z,
                                'update_donor_x' : self.update_donor_x,
                                'update_donor_y' : self.update_donor_y,
                                'update_zstage' : self.update_zstage,
                                'update_laser' : self.update_laser,
                                'update_super' : self.update_super,
                                'alive_donor' : self.donor_alive,
                                'alive_receiver' : self.receiver_alive,
                                'alive_laser' : self.laser_alive,
                                'alive_zstage' : self.zstage_alive,
                                }
        
#        self.actionClose.triggered.connect(self.close)
        self.pushButton_receiver_stepper_x_move_abs.clicked.connect(self.receiver_stepper_x_move_abs)
        self.lineEdit_receiver_stepper_x_move_abs.setValidator(QtGui.QDoubleValidator())
        self.lineEdit_receiver_stepper_x_move_abs.setText('0.000')  
        self.pushButton_receiver_stepper_x_move_rel.clicked.connect(self.receiver_stepper_x_move_rel)
        self.lineEdit_receiver_stepper_x_move_rel.setValidator(QtGui.QDoubleValidator())
        self.lineEdit_receiver_stepper_x_move_rel.setText('0.000')     
        self.pushButton_receiver_stepper_x_home.clicked.connect(self.receiver_stepper_x_home)
        
        self.pushButton_receiver_stepper_y_move_abs.clicked.connect(self.receiver_stepper_y_move_abs)
        self.lineEdit_receiver_stepper_y_move_abs.setValidator(QtGui.QDoubleValidator())
        self.lineEdit_receiver_stepper_y_move_abs.setText('0.000')  
        self.pushButton_receiver_stepper_y_move_rel.clicked.connect(self.receiver_stepper_y_move_rel)
        self.lineEdit_receiver_stepper_y_move_rel.setValidator(QtGui.QDoubleValidator())
        self.lineEdit_receiver_stepper_y_move_rel.setText('0.000')     
        self.pushButton_receiver_stepper_y_home.clicked.connect(self.receiver_stepper_y_home)
        
        self.pushButton_receiver_stepper_z_move_abs.clicked.connect(self.receiver_stepper_z_move_abs)
        self.lineEdit_receiver_stepper_z_move_abs.setValidator(QtGui.QDoubleValidator())
        self.lineEdit_receiver_stepper_z_move_abs.setText('0.000')  
        self.pushButton_receiver_stepper_z_move_rel.clicked.connect(self.receiver_stepper_z_move_rel)
        self.lineEdit_receiver_stepper_z_move_rel.setValidator(QtGui.QDoubleValidator())
        self.lineEdit_receiver_stepper_z_move_rel.setText('0.000')     
        self.pushButton_receiver_stepper_z_home.clicked.connect(self.receiver_stepper_z_home)
        
        self.pushButton_donor_x_move_abs.clicked.connect(self.donor_x_move_abs)
        self.lineEdit_donor_x_move_abs.setValidator(QtGui.QDoubleValidator())
        self.lineEdit_donor_x_move_abs.setText('0.000')  
        self.pushButton_donor_x_move_rel.clicked.connect(self.donor_x_move_rel)
        self.lineEdit_donor_x_move_rel.setValidator(QtGui.QDoubleValidator())
        self.lineEdit_donor_x_move_rel.setText('0.000')     
        self.pushButton_donor_x_home.clicked.connect(self.donor_x_home)
        
        self.pushButton_donor_y_move_abs.clicked.connect(self.donor_y_move_abs)
        self.lineEdit_donor_y_move_abs.setValidator(QtGui.QDoubleValidator())
        self.lineEdit_donor_y_move_abs.setText('0.000')  
        self.pushButton_donor_y_move_rel.clicked.connect(self.donor_y_move_rel)
        self.lineEdit_donor_y_move_rel.setValidator(QtGui.QDoubleValidator())
        self.lineEdit_donor_y_move_rel.setText('0.000')     
        self.pushButton_donor_y_home.clicked.connect(self.donor_y_home)

        self.pushButton_zstage_move_abs.clicked.connect(self.zstage_move_abs)
        self.lineEdit_zstage_move_abs.setValidator(QtGui.QDoubleValidator())
        self.lineEdit_zstage_move_abs.setText('0.000')  
        self.pushButton_zstage_move_rel.clicked.connect(self.zstage_move_rel)
        self.lineEdit_zstage_move_rel.setValidator(QtGui.QDoubleValidator())
        self.lineEdit_zstage_move_rel.setText('0.000')     
        self.pushButton_zstage_home.clicked.connect(self.zstage_home)

        self.pushButton_laser_power.clicked.connect(self.laser_setPower)
        self.lineEdit_laser_power.setValidator(QtGui.QDoubleValidator())
        self.lineEdit_laser_power.setText('0.000')  
        self.pushButton_laser_singlePulse.clicked.connect(self.laser_singlePulse)
        self.lineEdit_laser_numberPulses.setValidator(QtGui.QIntValidator())
        self.lineEdit_laser_numberPulses.setText('0')     
        self.pushButton_laser_multiPulse.clicked.connect(self.laser_multiPulse)
        self.pushButton_laser_on.clicked.connect(self.laser_on)  
        self.pushButton_laser_off.clicked.connect(self.laser_off)              
        
        self.pushButton_donor_ctrl_start.clicked.connect(self.donor_ctrl_start)
        self.pushButton_donor_ctrl_stop.clicked.connect(self.donor_ctrl_stop)
        self.lineEdit_donor_ctrl_status.setText('Off') 
        self.pushButton_receiver_ctrl_start.clicked.connect(self.receiver_ctrl_start)
        self.pushButton_receiver_ctrl_stop.clicked.connect(self.receiver_ctrl_stop)
        self.lineEdit_receiver_ctrl_status.setText('Off')   
        self.pushButton_zstage_ctrl_start.clicked.connect(self.zstage_ctrl_start)
        self.pushButton_zstage_ctrl_stop.clicked.connect(self.zstage_ctrl_stop)
        self.lineEdit_zstage_ctrl_status.setText('Off')
        self.pushButton_laser_ctrl_start.clicked.connect(self.laser_ctrl_start)
        self.pushButton_laser_ctrl_stop.clicked.connect(self.laser_ctrl_stop)
        self.lineEdit_laser_ctrl_status.setText('Off') 
  
        self.pushButton_super_print3D.clicked.connect(self.super_print3D)
        self.pushButton_super_energy.clicked.connect(self.super_energy)
        self.pushButton_super_focus.clicked.connect(self.super_focus)
        self.pushButton_super_pause.clicked.connect(self.super_pause)
        self.pushButton_super_stop.clicked.connect(self.super_stop)
        self.lineEdit_super_print3D_laserPower_2.setDisabled(True)
        self.checkBox_super_print3D.stateChanged.connect(self.super_multi)
        
        self.comboBox_global.currentIndexChanged.connect(self.global_show)
        self.pushButton_global.clicked.connect(self.global_set)
   
        self.lcdNumber_laser.setAutoFillBackground(True)
        p = self.lcdNumber_laser.palette()
        p.setColor(self.lcdNumber_laser.backgroundRole(), QtCore.Qt.white)
        self.lcdNumber_laser.setPalette(p)
        
        
    def status_loop(self):
        while self.active==True:
#            print 'status active'
            self.ctrl_status_update()
            time.sleep(0.005)
            
            if not self.status_q.empty():        
                item=self.status_q.get()
                self.update_options[item[0]](item[1])
                self.status_q.task_done()
        
    def run(self):
        self.active=True
        self.status_t.start()
        self.ctrl_super.run()

    def stop(self):
        self.active=False
        self.status_t.join()
        self.ctrl_super.stop()

    def ctrl_status_update(self):
        self.status_donor+=1
        self.status_receiver+=1
        self.status_laser+=1
        self.status_zstage+=1
        
        if self.status_donor > self.timeout_value:
            self.lineEdit_donor_ctrl_status.setText('Off') 
            self.tab_donor.setDisabled(True)
        else:
            self.lineEdit_donor_ctrl_status.setText('Active')
            self.tab_donor.setDisabled(False)

        if self.status_receiver > self.timeout_value:
            self.lineEdit_receiver_ctrl_status.setText('Off') 
            self.tab_receiver_stepper.setDisabled(True)
        else:
            self.lineEdit_receiver_ctrl_status.setText('Active')
            self.tab_receiver_stepper.setDisabled(False)

        if self.status_zstage > self.timeout_value:
            self.lineEdit_zstage_ctrl_status.setText('Off')            
            self.tab_z_stage.setDisabled(True)
       
        else:
            self.lineEdit_zstage_ctrl_status.setText('Active')
            self.tab_z_stage.setDisabled(False)

        if self.status_laser > self.timeout_value:
            self.lineEdit_laser_ctrl_status.setText('Off')
            self.tab_laser.setDisabled(True)
        else:
            self.lineEdit_laser_ctrl_status.setText('Active')
            self.tab_laser.setDisabled(False)               
        if self.status_zstage > self.timeout_value or self.status_laser > self.timeout_value or self.status_receiver > self.timeout_value or self.status_donor > self.timeout_value:
            self.tab_scripts.setDisabled(True)
        else:
            self.tab_scripts.setDisabled(False)
            
        return 0
      
    def laser_setPower(self):
#        print('Set laser power')
        self.laser_q.put(['update_laser_power',float(self.lineEdit_laser_power.text())],False)
        
    def laser_singlePulse(self):
        self.laser_q.put(['single_pulse',0],False)
        
    def laser_multiPulse(self):
        self.laser_q.put(['multi_pulse',int(self.lineEdit_laser_numberPulses.text())],False)
        
    def laser_on(self):
        self.laser_q.put(['laser_on',0],False)
        self.lcdNumber_laser.setAutoFillBackground(True)
        p = self.lcdNumber_laser.palette()
        p.setColor(self.lcdNumber_laser.backgroundRole(), QtCore.Qt.red)
        self.lcdNumber_laser.setPalette(p)
        
    def laser_off(self):
        self.laser_q.put(['laser_off',0],False)
        self.lcdNumber_laser.setAutoFillBackground(True)
        p = self.lcdNumber_laser.palette()
        p.setColor(self.lcdNumber_laser.backgroundRole(), QtCore.Qt.white)
        self.lcdNumber_laser.setPalette(p)
        
    def receiver_stepper_x_move_abs(self):
#        print("Command sent")
        self.receiver_q.put(['move_abs_x',float(self.lineEdit_receiver_stepper_x_move_abs.text())],False)
        
    def receiver_stepper_x_move_rel(self):
#        print("Command sent")
        self.receiver_q.put(['move_rel_x',float(self.lineEdit_receiver_stepper_x_move_rel.text())],False)
        
    def receiver_stepper_x_home(self):
#        print("Command sent")
        self.receiver_q.put(['home_x',0],False)
        
    def receiver_stepper_y_move_abs(self):
#        print("Command sent")
        self.receiver_q.put(['move_abs_y',float(self.lineEdit_receiver_stepper_y_move_abs.text())],False)
        
    def receiver_stepper_y_move_rel(self):
#        print("Command sent")
        self.receiver_q.put(['move_rel_y',float(self.lineEdit_receiver_stepper_y_move_rel.text())],False)
        
    def receiver_stepper_y_home(self):
#        print("Command sent")
        self.receiver_q.put(['home_y',0],False)
        
    def receiver_stepper_z_move_abs(self):
#        print("Command sent")
        self.receiver_q.put(['move_abs_z',float(self.lineEdit_receiver_stepper_z_move_abs.text())],False)
        
    def receiver_stepper_z_move_rel(self):
#        print("Command sent")
        self.receiver_q.put(['move_rel_z',float(self.lineEdit_receiver_stepper_z_move_rel.text())],False)
        
    def receiver_stepper_z_home(self):
#        print("Command sent")
        self.receiver_q.put(['home_z',0],False)
        
    def donor_x_move_abs(self):
#        print("Command sent")
        self.donor_q.put(['move_abs_x',float(self.lineEdit_donor_x_move_abs.text())],False)
        
    def donor_x_move_rel(self):
#        print("Command sent")
        self.donor_q.put(['move_rel_x',float(self.lineEdit_donor_x_move_rel.text())],False)
        
    def donor_x_home(self):
#        print("Command sent")
        self.donor_q.put(['home_x',0],False)
        
    def donor_y_move_abs(self):
#        print("Command sent")
        self.donor_q.put(['move_abs_y',float(self.lineEdit_donor_y_move_abs.text())],False)
        
    def donor_y_move_rel(self):
#        print("Command sent")
        self.donor_q.put(['move_rel_y',float(self.lineEdit_donor_y_move_rel.text())],False)
        
    def donor_y_home(self):
#        print("Command sent")
        self.donor_q.put(['home_y',0],False)
        
    def zstage_move_abs(self):
#        print("Command sent")
        self.zstage_q.put(['move_abs_z',float(self.lineEdit_zstage_move_abs.text())],False)
        
    def zstage_move_rel(self):
#        print("Command sent")
        self.zstage_q.put(['move_rel_z',float(self.lineEdit_zstage_move_rel.text())],False)
        
    def zstage_home(self):
#        print("Command sent")
        self.zstage_q.put(['home_z',0],False)
        
    def update_receiver_x(self,pos):
        self.lcdNumber_receiver_stepper_x.display(pos) 
        gb.gbl_dict['gbl_receiver_x_pos']=pos
               
    def update_receiver_y(self,pos):
        self.lcdNumber_receiver_stepper_y.display(pos) 
        gb.gbl_dict['gbl_receiver_y_pos']=pos
        
    def update_receiver_z(self,pos):
        self.lcdNumber_receiver_stepper_z.display(pos) 
        gb.gbl_dict['gbl_receiver_z_pos']=pos
        
    def update_donor_x(self,pos):
        self.lcdNumber_donor_x.display(pos) 
        gb.gbl_dict['gbl_donor_x_pos']=pos
        
    def update_donor_y(self,pos):
        self.lcdNumber_donor_y.display(pos) 
        gb.gbl_dict['gbl_donor_y_pos']=pos
        
    def update_zstage(self,pos):
        self.lcdNumber_zstage.display(pos) 
        gb.gbl_dict['gbl_zstage_pos']=pos
        
    def update_laser(self,pos):
        self.lcdNumber_laser.display(pos) 
        gb.gbl_dict['gbl_laser_pos']=pos
        
    def update_super(self,dummy):
#        dummy = [perc,time]
        self.lineEdit_super_perc.setText(str(int(dummy[0])))
        self.lineEdit_super_time.setText(str(round(dummy[1],1)))

        
    def donor_ctrl_start(self):
        if self.status_donor > self.timeout_value:
            try:
                self.ctrl_donor=ctrl_donor.control_donor(self.donor_q,self.status_q)
                self.ctrl_donor.run()
            except:
                print("ERROR: Starting DONOR_CTRL")
               
    def donor_ctrl_stop(self):
        if self.status_donor <= self.timeout_value:
            self.ctrl_donor.stop()
       
    def receiver_ctrl_start(self):
        if self.status_receiver > self.timeout_value:
            try:
                self.ctrl_receiver=ctrl_receiver.control_receiver(self.receiver_q,self.status_q)
                self.ctrl_receiver.run()
            except:
                print("ERROR: Starting RECEIVER_CTRL")
       
    def receiver_ctrl_stop(self):
        if self.status_receiver <= self.timeout_value:
            self.ctrl_receiver.stop()
   
    def zstage_ctrl_start(self):
        if self.status_zstage > self.timeout_value:
            try:
                self.ctrl_zstage=ctrl_zstage.control_zstage(self.zstage_q,self.status_q)
                self.ctrl_zstage.run()
            except:
                print("ERROR: Starting ZSTAGE_CTRL")
        
    def zstage_ctrl_stop(self):
        if self.status_zstage <= self.timeout_value:
            self.ctrl_zstage.stop()
           
    def laser_ctrl_start(self):
        if self.status_laser > self.timeout_value:
            try:
                self.ctrl_laser=ctrl_laser.control_laser(self.laser_q,self.status_q)
                self.ctrl_laser.run()
            except:
                print("ERROR: Starting LASER_CTRL")
        
    def laser_ctrl_stop(self):
        if self.status_laser <= self.timeout_value:
            self.ctrl_laser.stop()

    def donor_alive(self,dummy):
        self.status_donor=dummy

    def receiver_alive(self,dummy):
        self.status_receiver=dummy

    def laser_alive(self,dummy):
        self.status_laser=dummy

    def zstage_alive(self,dummy):
        self.status_zstage=dummy
    
    def super_print3D(self):
        if self.checkBox_super_print3D.isChecked():
            arg=[float(self.lineEdit_super_print3D_laserPower.text()),float(self.lineEdit_super_print3D_laserPower_2.text())]
            self.super_q.put(['print3D_multi',arg],False)
        else:
            arg=[float(self.lineEdit_super_print3D_laserPower.text())]
            self.super_q.put(['print3D',arg],False)
    
    def super_energy(self):
        energy_min=float(self.lineEdit_super_energy_laser_min.text())
        energy_max=float(self.lineEdit_super_energy_laser_max.text())
        delta=float(self.lineEdit_super_energy_laser_delta.text())
        number=float(self.lineEdit_super_energy_number.text())
        spatial=float(self.lineEdit_super_energy_spatial.text())
        arg=[energy_min,energy_max,delta,number,spatial]
        
        self.super_q.put(['energy',arg],False) 
    
    def super_focus(self):
        z_min=float(self.lineEdit_super_focus_z_min.text())
        z_max=float(self.lineEdit_super_focus_z_max.text())
        z_delta=float(self.lineEdit_super_focus_z_delta.text())
        laser_power = float(self.lineEdit_super_focus_power.text())
        number=float(self.lineEdit_super_focus_number.text())
        spatial=float(self.lineEdit_super_focus_spatial.text())
        arg=[z_min,z_max,z_delta,laser_power,number,spatial]
        
        self.super_q.put(['focus',arg],False)
        
    def super_pause(self):
        gb.gbl_dict['gbl_super_pause'] = not gb.gbl_dict['gbl_super_pause']
        if gb.gbl_dict['gbl_super_pause']:
            self.pushButton_super_pause.setText('RESUME')
        else:
            self.pushButton_super_pause.setText('PAUSE')
            
    def super_stop(self):
        gb.gbl_dict['gbl_super_stop'] = not gb.gbl_dict['gbl_super_stop']

    def super_multi(self):
        self.lineEdit_super_print3D_laserPower_2.setDisabled(not self.checkBox_super_print3D.isChecked())
        
    def global_show(self):
        self.lineEdit_global.setText(str(gb.gbl_dict[str(self.comboBox_global.currentText())]))
        
    def global_set(self):
        if type (gb.gbl_dict[str(self.comboBox_global.currentText())]) is bool:
            gb.gbl_dict[str(self.comboBox_global.currentText())] = bool(float(self.lineEdit_global.text()))       
        else:
            gb.gbl_dict[str(self.comboBox_global.currentText())] = float(self.lineEdit_global.text())

        
    
def main():
    app = QtGui.QApplication(sys.argv)  
    form = MainApp()
    form.run()
    form.show()                         
    app.exec_()
    form.stop()
    
    time.sleep(1)



if __name__ == '__main__':              
    main()  
