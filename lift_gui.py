# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LIFT_GUI.ui'
#
# Created: Thu Mar 30 15:31:53 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 593)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 541))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_general = QtGui.QWidget()
        self.tab_general.setObjectName(_fromUtf8("tab_general"))
        self.groupBox = QtGui.QGroupBox(self.tab_general)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 751, 201))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.pushButton_laser_ctrl_stop = QtGui.QPushButton(self.groupBox)
        self.pushButton_laser_ctrl_stop.setGeometry(QtCore.QRect(430, 130, 93, 28))
        self.pushButton_laser_ctrl_stop.setObjectName(_fromUtf8("pushButton_laser_ctrl_stop"))
        self.lineEdit_zstage_ctrl_status = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_zstage_ctrl_status.setEnabled(False)
        self.lineEdit_zstage_ctrl_status.setGeometry(QtCore.QRect(102, 60, 91, 22))
        self.lineEdit_zstage_ctrl_status.setFrame(True)
        self.lineEdit_zstage_ctrl_status.setReadOnly(True)
        self.lineEdit_zstage_ctrl_status.setObjectName(_fromUtf8("lineEdit_zstage_ctrl_status"))
        self.label_zstage_ctrl = QtGui.QLabel(self.groupBox)
        self.label_zstage_ctrl.setGeometry(QtCore.QRect(110, 30, 91, 16))
        self.label_zstage_ctrl.setObjectName(_fromUtf8("label_zstage_ctrl"))
        self.label_donor_ctrl = QtGui.QLabel(self.groupBox)
        self.label_donor_ctrl.setGeometry(QtCore.QRect(220, 30, 81, 16))
        self.label_donor_ctrl.setObjectName(_fromUtf8("label_donor_ctrl"))
        self.lineEdit_donor_ctrl_status = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_donor_ctrl_status.setEnabled(False)
        self.lineEdit_donor_ctrl_status.setGeometry(QtCore.QRect(212, 60, 91, 22))
        self.lineEdit_donor_ctrl_status.setReadOnly(True)
        self.lineEdit_donor_ctrl_status.setObjectName(_fromUtf8("lineEdit_donor_ctrl_status"))
        self.pushButton_donor_ctrl_start = QtGui.QPushButton(self.groupBox)
        self.pushButton_donor_ctrl_start.setGeometry(QtCore.QRect(210, 90, 93, 28))
        self.pushButton_donor_ctrl_start.setObjectName(_fromUtf8("pushButton_donor_ctrl_start"))
        self.lineEdit_laser_ctrl_status = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_laser_ctrl_status.setEnabled(False)
        self.lineEdit_laser_ctrl_status.setGeometry(QtCore.QRect(432, 60, 91, 22))
        self.lineEdit_laser_ctrl_status.setReadOnly(True)
        self.lineEdit_laser_ctrl_status.setObjectName(_fromUtf8("lineEdit_laser_ctrl_status"))
        self.pushButton_laser_ctrl_start = QtGui.QPushButton(self.groupBox)
        self.pushButton_laser_ctrl_start.setGeometry(QtCore.QRect(430, 90, 93, 28))
        self.pushButton_laser_ctrl_start.setObjectName(_fromUtf8("pushButton_laser_ctrl_start"))
        self.pushButton_receiver_ctrl_stop = QtGui.QPushButton(self.groupBox)
        self.pushButton_receiver_ctrl_stop.setGeometry(QtCore.QRect(318, 130, 93, 28))
        self.pushButton_receiver_ctrl_stop.setObjectName(_fromUtf8("pushButton_receiver_ctrl_stop"))
        self.pushButton_zstage_ctrl_start = QtGui.QPushButton(self.groupBox)
        self.pushButton_zstage_ctrl_start.setGeometry(QtCore.QRect(100, 90, 93, 28))
        self.pushButton_zstage_ctrl_start.setObjectName(_fromUtf8("pushButton_zstage_ctrl_start"))
        self.lineEdit_receiver_ctrl_status = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_receiver_ctrl_status.setEnabled(False)
        self.lineEdit_receiver_ctrl_status.setGeometry(QtCore.QRect(320, 60, 91, 22))
        self.lineEdit_receiver_ctrl_status.setReadOnly(True)
        self.lineEdit_receiver_ctrl_status.setObjectName(_fromUtf8("lineEdit_receiver_ctrl_status"))
        self.label_reveiver_ctrl = QtGui.QLabel(self.groupBox)
        self.label_reveiver_ctrl.setGeometry(QtCore.QRect(320, 30, 101, 16))
        self.label_reveiver_ctrl.setObjectName(_fromUtf8("label_reveiver_ctrl"))
        self.pushButton_zstage_ctrl_stop = QtGui.QPushButton(self.groupBox)
        self.pushButton_zstage_ctrl_stop.setGeometry(QtCore.QRect(100, 130, 93, 28))
        self.pushButton_zstage_ctrl_stop.setObjectName(_fromUtf8("pushButton_zstage_ctrl_stop"))
        self.pushButton_donor_ctrl_stop = QtGui.QPushButton(self.groupBox)
        self.pushButton_donor_ctrl_stop.setGeometry(QtCore.QRect(210, 130, 93, 28))
        self.pushButton_donor_ctrl_stop.setObjectName(_fromUtf8("pushButton_donor_ctrl_stop"))
        self.pushButton_receiver_ctrl_start = QtGui.QPushButton(self.groupBox)
        self.pushButton_receiver_ctrl_start.setGeometry(QtCore.QRect(318, 90, 93, 28))
        self.pushButton_receiver_ctrl_start.setObjectName(_fromUtf8("pushButton_receiver_ctrl_start"))
        self.label_laser_ctrl = QtGui.QLabel(self.groupBox)
        self.label_laser_ctrl.setGeometry(QtCore.QRect(440, 30, 81, 16))
        self.label_laser_ctrl.setObjectName(_fromUtf8("label_laser_ctrl"))
        self.tabWidget.addTab(self.tab_general, _fromUtf8(""))
        self.tab_z_stage = QtGui.QWidget()
        self.tab_z_stage.setObjectName(_fromUtf8("tab_z_stage"))
        self.groupBox_zstage = QtGui.QGroupBox(self.tab_z_stage)
        self.groupBox_zstage.setGeometry(QtCore.QRect(20, 10, 751, 161))
        self.groupBox_zstage.setObjectName(_fromUtf8("groupBox_zstage"))
        self.lcdNumber_zstage = QtGui.QLCDNumber(self.groupBox_zstage)
        self.lcdNumber_zstage.setGeometry(QtCore.QRect(20, 30, 121, 23))
        self.lcdNumber_zstage.setFrameShadow(QtGui.QFrame.Plain)
        self.lcdNumber_zstage.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdNumber_zstage.setObjectName(_fromUtf8("lcdNumber_zstage"))
        self.pushButton_zstage_home = QtGui.QPushButton(self.groupBox_zstage)
        self.pushButton_zstage_home.setGeometry(QtCore.QRect(20, 60, 121, 28))
        self.pushButton_zstage_home.setObjectName(_fromUtf8("pushButton_zstage_home"))
        self.pushButton_zstage_move_rel = QtGui.QPushButton(self.groupBox_zstage)
        self.pushButton_zstage_move_rel.setGeometry(QtCore.QRect(160, 60, 111, 28))
        self.pushButton_zstage_move_rel.setObjectName(_fromUtf8("pushButton_zstage_move_rel"))
        self.lineEdit_zstage_move_rel = QtGui.QLineEdit(self.groupBox_zstage)
        self.lineEdit_zstage_move_rel.setGeometry(QtCore.QRect(160, 30, 113, 22))
        self.lineEdit_zstage_move_rel.setObjectName(_fromUtf8("lineEdit_zstage_move_rel"))
        self.lineEdit_zstage_move_abs = QtGui.QLineEdit(self.groupBox_zstage)
        self.lineEdit_zstage_move_abs.setGeometry(QtCore.QRect(290, 30, 113, 22))
        self.lineEdit_zstage_move_abs.setObjectName(_fromUtf8("lineEdit_zstage_move_abs"))
        self.pushButton_zstage_move_abs = QtGui.QPushButton(self.groupBox_zstage)
        self.pushButton_zstage_move_abs.setGeometry(QtCore.QRect(290, 60, 111, 28))
        self.pushButton_zstage_move_abs.setObjectName(_fromUtf8("pushButton_zstage_move_abs"))
        self.tabWidget.addTab(self.tab_z_stage, _fromUtf8(""))
        self.tab_donor = QtGui.QWidget()
        self.tab_donor.setObjectName(_fromUtf8("tab_donor"))
        self.groupBox_donor_x = QtGui.QGroupBox(self.tab_donor)
        self.groupBox_donor_x.setGeometry(QtCore.QRect(20, 10, 751, 161))
        self.groupBox_donor_x.setObjectName(_fromUtf8("groupBox_donor_x"))
        self.lcdNumber_donor_x = QtGui.QLCDNumber(self.groupBox_donor_x)
        self.lcdNumber_donor_x.setGeometry(QtCore.QRect(20, 30, 121, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.lcdNumber_donor_x.setFont(font)
        self.lcdNumber_donor_x.setFrameShape(QtGui.QFrame.Box)
        self.lcdNumber_donor_x.setFrameShadow(QtGui.QFrame.Plain)
        self.lcdNumber_donor_x.setSmallDecimalPoint(False)
        self.lcdNumber_donor_x.setNumDigits(5)
        self.lcdNumber_donor_x.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdNumber_donor_x.setObjectName(_fromUtf8("lcdNumber_donor_x"))
        self.pushButton_donor_x_home = QtGui.QPushButton(self.groupBox_donor_x)
        self.pushButton_donor_x_home.setGeometry(QtCore.QRect(20, 60, 121, 28))
        self.pushButton_donor_x_home.setObjectName(_fromUtf8("pushButton_donor_x_home"))
        self.pushButton_donor_x_move_rel = QtGui.QPushButton(self.groupBox_donor_x)
        self.pushButton_donor_x_move_rel.setGeometry(QtCore.QRect(160, 60, 111, 28))
        self.pushButton_donor_x_move_rel.setObjectName(_fromUtf8("pushButton_donor_x_move_rel"))
        self.lineEdit_donor_x_move_rel = QtGui.QLineEdit(self.groupBox_donor_x)
        self.lineEdit_donor_x_move_rel.setGeometry(QtCore.QRect(160, 30, 113, 22))
        self.lineEdit_donor_x_move_rel.setObjectName(_fromUtf8("lineEdit_donor_x_move_rel"))
        self.lineEdit_donor_x_move_abs = QtGui.QLineEdit(self.groupBox_donor_x)
        self.lineEdit_donor_x_move_abs.setGeometry(QtCore.QRect(290, 30, 113, 22))
        self.lineEdit_donor_x_move_abs.setObjectName(_fromUtf8("lineEdit_donor_x_move_abs"))
        self.pushButton_donor_x_move_abs = QtGui.QPushButton(self.groupBox_donor_x)
        self.pushButton_donor_x_move_abs.setGeometry(QtCore.QRect(290, 60, 111, 28))
        self.pushButton_donor_x_move_abs.setObjectName(_fromUtf8("pushButton_donor_x_move_abs"))
        self.groupBox_donor_y = QtGui.QGroupBox(self.tab_donor)
        self.groupBox_donor_y.setGeometry(QtCore.QRect(20, 180, 751, 161))
        self.groupBox_donor_y.setObjectName(_fromUtf8("groupBox_donor_y"))
        self.lcdNumber_donor_y = QtGui.QLCDNumber(self.groupBox_donor_y)
        self.lcdNumber_donor_y.setGeometry(QtCore.QRect(20, 30, 121, 23))
        self.lcdNumber_donor_y.setFrameShadow(QtGui.QFrame.Plain)
        self.lcdNumber_donor_y.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdNumber_donor_y.setObjectName(_fromUtf8("lcdNumber_donor_y"))
        self.pushButton_donor_y_home = QtGui.QPushButton(self.groupBox_donor_y)
        self.pushButton_donor_y_home.setGeometry(QtCore.QRect(20, 60, 121, 28))
        self.pushButton_donor_y_home.setObjectName(_fromUtf8("pushButton_donor_y_home"))
        self.pushButton_donor_y_move_rel = QtGui.QPushButton(self.groupBox_donor_y)
        self.pushButton_donor_y_move_rel.setGeometry(QtCore.QRect(160, 60, 111, 28))
        self.pushButton_donor_y_move_rel.setObjectName(_fromUtf8("pushButton_donor_y_move_rel"))
        self.lineEdit_donor_y_move_rel = QtGui.QLineEdit(self.groupBox_donor_y)
        self.lineEdit_donor_y_move_rel.setGeometry(QtCore.QRect(160, 30, 113, 22))
        self.lineEdit_donor_y_move_rel.setObjectName(_fromUtf8("lineEdit_donor_y_move_rel"))
        self.lineEdit_donor_y_move_abs = QtGui.QLineEdit(self.groupBox_donor_y)
        self.lineEdit_donor_y_move_abs.setGeometry(QtCore.QRect(290, 30, 113, 22))
        self.lineEdit_donor_y_move_abs.setObjectName(_fromUtf8("lineEdit_donor_y_move_abs"))
        self.pushButton_donor_y_move_abs = QtGui.QPushButton(self.groupBox_donor_y)
        self.pushButton_donor_y_move_abs.setGeometry(QtCore.QRect(290, 60, 111, 28))
        self.pushButton_donor_y_move_abs.setObjectName(_fromUtf8("pushButton_donor_y_move_abs"))
        self.tabWidget.addTab(self.tab_donor, _fromUtf8(""))
        self.tab_receiver_stepper = QtGui.QWidget()
        self.tab_receiver_stepper.setObjectName(_fromUtf8("tab_receiver_stepper"))
        self.groupBox_receiver_stepper_x = QtGui.QGroupBox(self.tab_receiver_stepper)
        self.groupBox_receiver_stepper_x.setGeometry(QtCore.QRect(20, 10, 751, 161))
        self.groupBox_receiver_stepper_x.setObjectName(_fromUtf8("groupBox_receiver_stepper_x"))
        self.lcdNumber_receiver_stepper_x = QtGui.QLCDNumber(self.groupBox_receiver_stepper_x)
        self.lcdNumber_receiver_stepper_x.setGeometry(QtCore.QRect(20, 30, 121, 23))
        self.lcdNumber_receiver_stepper_x.setFrameShadow(QtGui.QFrame.Plain)
        self.lcdNumber_receiver_stepper_x.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdNumber_receiver_stepper_x.setObjectName(_fromUtf8("lcdNumber_receiver_stepper_x"))
        self.pushButton_receiver_stepper_x_home = QtGui.QPushButton(self.groupBox_receiver_stepper_x)
        self.pushButton_receiver_stepper_x_home.setGeometry(QtCore.QRect(20, 60, 121, 28))
        self.pushButton_receiver_stepper_x_home.setObjectName(_fromUtf8("pushButton_receiver_stepper_x_home"))
        self.pushButton_receiver_stepper_x_move_rel = QtGui.QPushButton(self.groupBox_receiver_stepper_x)
        self.pushButton_receiver_stepper_x_move_rel.setGeometry(QtCore.QRect(160, 60, 111, 28))
        self.pushButton_receiver_stepper_x_move_rel.setObjectName(_fromUtf8("pushButton_receiver_stepper_x_move_rel"))
        self.lineEdit_receiver_stepper_x_move_rel = QtGui.QLineEdit(self.groupBox_receiver_stepper_x)
        self.lineEdit_receiver_stepper_x_move_rel.setGeometry(QtCore.QRect(160, 30, 113, 22))
        self.lineEdit_receiver_stepper_x_move_rel.setObjectName(_fromUtf8("lineEdit_receiver_stepper_x_move_rel"))
        self.lineEdit_receiver_stepper_x_move_abs = QtGui.QLineEdit(self.groupBox_receiver_stepper_x)
        self.lineEdit_receiver_stepper_x_move_abs.setGeometry(QtCore.QRect(290, 30, 113, 22))
        self.lineEdit_receiver_stepper_x_move_abs.setObjectName(_fromUtf8("lineEdit_receiver_stepper_x_move_abs"))
        self.pushButton_receiver_stepper_x_move_abs = QtGui.QPushButton(self.groupBox_receiver_stepper_x)
        self.pushButton_receiver_stepper_x_move_abs.setGeometry(QtCore.QRect(290, 60, 111, 28))
        self.pushButton_receiver_stepper_x_move_abs.setObjectName(_fromUtf8("pushButton_receiver_stepper_x_move_abs"))
        self.groupBox_receiver_stepper_y = QtGui.QGroupBox(self.tab_receiver_stepper)
        self.groupBox_receiver_stepper_y.setGeometry(QtCore.QRect(20, 180, 751, 161))
        self.groupBox_receiver_stepper_y.setObjectName(_fromUtf8("groupBox_receiver_stepper_y"))
        self.lcdNumber_receiver_stepper_y = QtGui.QLCDNumber(self.groupBox_receiver_stepper_y)
        self.lcdNumber_receiver_stepper_y.setGeometry(QtCore.QRect(20, 30, 121, 23))
        self.lcdNumber_receiver_stepper_y.setFrameShadow(QtGui.QFrame.Plain)
        self.lcdNumber_receiver_stepper_y.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdNumber_receiver_stepper_y.setObjectName(_fromUtf8("lcdNumber_receiver_stepper_y"))
        self.pushButton_receiver_stepper_y_home = QtGui.QPushButton(self.groupBox_receiver_stepper_y)
        self.pushButton_receiver_stepper_y_home.setGeometry(QtCore.QRect(20, 60, 121, 28))
        self.pushButton_receiver_stepper_y_home.setObjectName(_fromUtf8("pushButton_receiver_stepper_y_home"))
        self.pushButton_receiver_stepper_y_move_rel = QtGui.QPushButton(self.groupBox_receiver_stepper_y)
        self.pushButton_receiver_stepper_y_move_rel.setGeometry(QtCore.QRect(160, 60, 111, 28))
        self.pushButton_receiver_stepper_y_move_rel.setObjectName(_fromUtf8("pushButton_receiver_stepper_y_move_rel"))
        self.lineEdit_receiver_stepper_y_move_rel = QtGui.QLineEdit(self.groupBox_receiver_stepper_y)
        self.lineEdit_receiver_stepper_y_move_rel.setGeometry(QtCore.QRect(160, 30, 113, 22))
        self.lineEdit_receiver_stepper_y_move_rel.setObjectName(_fromUtf8("lineEdit_receiver_stepper_y_move_rel"))
        self.lineEdit_receiver_stepper_y_move_abs = QtGui.QLineEdit(self.groupBox_receiver_stepper_y)
        self.lineEdit_receiver_stepper_y_move_abs.setGeometry(QtCore.QRect(290, 30, 113, 22))
        self.lineEdit_receiver_stepper_y_move_abs.setObjectName(_fromUtf8("lineEdit_receiver_stepper_y_move_abs"))
        self.pushButton_receiver_stepper_y_move_abs = QtGui.QPushButton(self.groupBox_receiver_stepper_y)
        self.pushButton_receiver_stepper_y_move_abs.setGeometry(QtCore.QRect(290, 60, 111, 28))
        self.pushButton_receiver_stepper_y_move_abs.setObjectName(_fromUtf8("pushButton_receiver_stepper_y_move_abs"))
        self.groupBox_receiver_stepper_z = QtGui.QGroupBox(self.tab_receiver_stepper)
        self.groupBox_receiver_stepper_z.setGeometry(QtCore.QRect(20, 350, 751, 161))
        self.groupBox_receiver_stepper_z.setObjectName(_fromUtf8("groupBox_receiver_stepper_z"))
        self.lcdNumber_receiver_stepper_z = QtGui.QLCDNumber(self.groupBox_receiver_stepper_z)
        self.lcdNumber_receiver_stepper_z.setGeometry(QtCore.QRect(20, 30, 121, 23))
        self.lcdNumber_receiver_stepper_z.setFrameShadow(QtGui.QFrame.Plain)
        self.lcdNumber_receiver_stepper_z.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdNumber_receiver_stepper_z.setObjectName(_fromUtf8("lcdNumber_receiver_stepper_z"))
        self.pushButton_receiver_stepper_z_home = QtGui.QPushButton(self.groupBox_receiver_stepper_z)
        self.pushButton_receiver_stepper_z_home.setGeometry(QtCore.QRect(20, 60, 121, 28))
        self.pushButton_receiver_stepper_z_home.setObjectName(_fromUtf8("pushButton_receiver_stepper_z_home"))
        self.pushButton_receiver_stepper_z_move_rel = QtGui.QPushButton(self.groupBox_receiver_stepper_z)
        self.pushButton_receiver_stepper_z_move_rel.setGeometry(QtCore.QRect(160, 60, 111, 28))
        self.pushButton_receiver_stepper_z_move_rel.setObjectName(_fromUtf8("pushButton_receiver_stepper_z_move_rel"))
        self.lineEdit_receiver_stepper_z_move_rel = QtGui.QLineEdit(self.groupBox_receiver_stepper_z)
        self.lineEdit_receiver_stepper_z_move_rel.setGeometry(QtCore.QRect(160, 30, 113, 22))
        self.lineEdit_receiver_stepper_z_move_rel.setObjectName(_fromUtf8("lineEdit_receiver_stepper_z_move_rel"))
        self.lineEdit_receiver_stepper_z_move_abs = QtGui.QLineEdit(self.groupBox_receiver_stepper_z)
        self.lineEdit_receiver_stepper_z_move_abs.setGeometry(QtCore.QRect(290, 30, 113, 22))
        self.lineEdit_receiver_stepper_z_move_abs.setObjectName(_fromUtf8("lineEdit_receiver_stepper_z_move_abs"))
        self.pushButton_receiver_stepper_z_move_abs = QtGui.QPushButton(self.groupBox_receiver_stepper_z)
        self.pushButton_receiver_stepper_z_move_abs.setGeometry(QtCore.QRect(290, 60, 111, 28))
        self.pushButton_receiver_stepper_z_move_abs.setObjectName(_fromUtf8("pushButton_receiver_stepper_z_move_abs"))
        self.tabWidget.addTab(self.tab_receiver_stepper, _fromUtf8(""))
        self.tab_laser = QtGui.QWidget()
        self.tab_laser.setObjectName(_fromUtf8("tab_laser"))
        self.groupBox_laser = QtGui.QGroupBox(self.tab_laser)
        self.groupBox_laser.setGeometry(QtCore.QRect(20, 20, 751, 161))
        self.groupBox_laser.setObjectName(_fromUtf8("groupBox_laser"))
        self.lcdNumber_laser = QtGui.QLCDNumber(self.groupBox_laser)
        self.lcdNumber_laser.setGeometry(QtCore.QRect(30, 40, 121, 23))
        self.lcdNumber_laser.setFrameShadow(QtGui.QFrame.Plain)
        self.lcdNumber_laser.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdNumber_laser.setObjectName(_fromUtf8("lcdNumber_laser"))
        self.pushButton_laser_power = QtGui.QPushButton(self.groupBox_laser)
        self.pushButton_laser_power.setGeometry(QtCore.QRect(170, 67, 121, 31))
        self.pushButton_laser_power.setObjectName(_fromUtf8("pushButton_laser_power"))
        self.pushButton_laser_singlePulse = QtGui.QPushButton(self.groupBox_laser)
        self.pushButton_laser_singlePulse.setGeometry(QtCore.QRect(300, 100, 111, 31))
        self.pushButton_laser_singlePulse.setObjectName(_fromUtf8("pushButton_laser_singlePulse"))
        self.lineEdit_laser_power = QtGui.QLineEdit(self.groupBox_laser)
        self.lineEdit_laser_power.setGeometry(QtCore.QRect(170, 40, 121, 22))
        self.lineEdit_laser_power.setObjectName(_fromUtf8("lineEdit_laser_power"))
        self.lineEdit_laser_numberPulses = QtGui.QLineEdit(self.groupBox_laser)
        self.lineEdit_laser_numberPulses.setGeometry(QtCore.QRect(300, 40, 113, 22))
        self.lineEdit_laser_numberPulses.setObjectName(_fromUtf8("lineEdit_laser_numberPulses"))
        self.pushButton_laser_multiPulse = QtGui.QPushButton(self.groupBox_laser)
        self.pushButton_laser_multiPulse.setGeometry(QtCore.QRect(300, 67, 111, 31))
        self.pushButton_laser_multiPulse.setObjectName(_fromUtf8("pushButton_laser_multiPulse"))
        self.pushButton_laser_on = QtGui.QPushButton(self.groupBox_laser)
        self.pushButton_laser_on.setGeometry(QtCore.QRect(30, 67, 121, 31))
        self.pushButton_laser_on.setObjectName(_fromUtf8("pushButton_laser_on"))
        self.pushButton_laser_off = QtGui.QPushButton(self.groupBox_laser)
        self.pushButton_laser_off.setGeometry(QtCore.QRect(30, 100, 261, 31))
        self.pushButton_laser_off.setObjectName(_fromUtf8("pushButton_laser_off"))
        self.label = QtGui.QLabel(self.groupBox_laser)
        self.label.setGeometry(QtCore.QRect(170, 20, 121, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox_laser)
        self.label_2.setGeometry(QtCore.QRect(300, 20, 121, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.groupBox_laser)
        self.label_3.setGeometry(QtCore.QRect(80, 20, 46, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.tabWidget.addTab(self.tab_laser, _fromUtf8(""))
        self.tab_scripts = QtGui.QWidget()
        self.tab_scripts.setObjectName(_fromUtf8("tab_scripts"))
        self.groupBox_scripts_print3D = QtGui.QGroupBox(self.tab_scripts)
        self.groupBox_scripts_print3D.setGeometry(QtCore.QRect(30, 20, 741, 80))
        self.groupBox_scripts_print3D.setObjectName(_fromUtf8("groupBox_scripts_print3D"))
        self.pushButton_super_print3D = QtGui.QPushButton(self.groupBox_scripts_print3D)
        self.pushButton_super_print3D.setGeometry(QtCore.QRect(20, 30, 93, 28))
        self.pushButton_super_print3D.setObjectName(_fromUtf8("pushButton_super_print3D"))
        self.lineEdit_super_print3D_laserPower = QtGui.QLineEdit(self.groupBox_scripts_print3D)
        self.lineEdit_super_print3D_laserPower.setGeometry(QtCore.QRect(240, 40, 113, 21))
        self.lineEdit_super_print3D_laserPower.setObjectName(_fromUtf8("lineEdit_super_print3D_laserPower"))
        self.label_4 = QtGui.QLabel(self.groupBox_scripts_print3D)
        self.label_4.setGeometry(QtCore.QRect(250, 20, 101, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.groupBox_scripts_print3D_2 = QtGui.QGroupBox(self.tab_scripts)
        self.groupBox_scripts_print3D_2.setGeometry(QtCore.QRect(30, 110, 741, 131))
        self.groupBox_scripts_print3D_2.setObjectName(_fromUtf8("groupBox_scripts_print3D_2"))
        self.pushButton_super_energy = QtGui.QPushButton(self.groupBox_scripts_print3D_2)
        self.pushButton_super_energy.setGeometry(QtCore.QRect(20, 30, 93, 28))
        self.pushButton_super_energy.setObjectName(_fromUtf8("pushButton_super_energy"))
        self.label_5 = QtGui.QLabel(self.groupBox_scripts_print3D_2)
        self.label_5.setGeometry(QtCore.QRect(240, 20, 111, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lineEdit_super_energy_laser_min = QtGui.QLineEdit(self.groupBox_scripts_print3D_2)
        self.lineEdit_super_energy_laser_min.setGeometry(QtCore.QRect(240, 40, 113, 21))
        self.lineEdit_super_energy_laser_min.setObjectName(_fromUtf8("lineEdit_super_energy_laser_min"))
        self.lineEdit_super_energy_laser_max = QtGui.QLineEdit(self.groupBox_scripts_print3D_2)
        self.lineEdit_super_energy_laser_max.setGeometry(QtCore.QRect(370, 40, 113, 21))
        self.lineEdit_super_energy_laser_max.setObjectName(_fromUtf8("lineEdit_super_energy_laser_max"))
        self.label_6 = QtGui.QLabel(self.groupBox_scripts_print3D_2)
        self.label_6.setGeometry(QtCore.QRect(370, 20, 121, 20))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lineEdit_super_energy_laser_delta = QtGui.QLineEdit(self.groupBox_scripts_print3D_2)
        self.lineEdit_super_energy_laser_delta.setGeometry(QtCore.QRect(500, 40, 113, 21))
        self.lineEdit_super_energy_laser_delta.setObjectName(_fromUtf8("lineEdit_super_energy_laser_delta"))
        self.label_7 = QtGui.QLabel(self.groupBox_scripts_print3D_2)
        self.label_7.setGeometry(QtCore.QRect(500, 20, 131, 20))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_12 = QtGui.QLabel(self.groupBox_scripts_print3D_2)
        self.label_12.setGeometry(QtCore.QRect(240, 70, 111, 20))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.lineEdit_super_energy_number = QtGui.QLineEdit(self.groupBox_scripts_print3D_2)
        self.lineEdit_super_energy_number.setGeometry(QtCore.QRect(240, 90, 113, 21))
        self.lineEdit_super_energy_number.setObjectName(_fromUtf8("lineEdit_super_energy_number"))
        self.label_13 = QtGui.QLabel(self.groupBox_scripts_print3D_2)
        self.label_13.setGeometry(QtCore.QRect(370, 70, 131, 20))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.lineEdit_super_energy_spatial = QtGui.QLineEdit(self.groupBox_scripts_print3D_2)
        self.lineEdit_super_energy_spatial.setGeometry(QtCore.QRect(370, 90, 113, 21))
        self.lineEdit_super_energy_spatial.setObjectName(_fromUtf8("lineEdit_super_energy_spatial"))
        self.groupBox_scripts_print3D_3 = QtGui.QGroupBox(self.tab_scripts)
        self.groupBox_scripts_print3D_3.setGeometry(QtCore.QRect(30, 250, 741, 131))
        self.groupBox_scripts_print3D_3.setObjectName(_fromUtf8("groupBox_scripts_print3D_3"))
        self.pushButton_super_focus = QtGui.QPushButton(self.groupBox_scripts_print3D_3)
        self.pushButton_super_focus.setGeometry(QtCore.QRect(20, 30, 93, 28))
        self.pushButton_super_focus.setObjectName(_fromUtf8("pushButton_super_focus"))
        self.label_8 = QtGui.QLabel(self.groupBox_scripts_print3D_3)
        self.label_8.setGeometry(QtCore.QRect(250, 20, 111, 20))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.lineEdit_super_focus_z_min = QtGui.QLineEdit(self.groupBox_scripts_print3D_3)
        self.lineEdit_super_focus_z_min.setGeometry(QtCore.QRect(240, 40, 113, 21))
        self.lineEdit_super_focus_z_min.setObjectName(_fromUtf8("lineEdit_super_focus_z_min"))
        self.lineEdit_super_focus_z_max = QtGui.QLineEdit(self.groupBox_scripts_print3D_3)
        self.lineEdit_super_focus_z_max.setGeometry(QtCore.QRect(370, 40, 113, 21))
        self.lineEdit_super_focus_z_max.setObjectName(_fromUtf8("lineEdit_super_focus_z_max"))
        self.label_9 = QtGui.QLabel(self.groupBox_scripts_print3D_3)
        self.label_9.setGeometry(QtCore.QRect(380, 20, 121, 20))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.lineEdit_super_focus_z_delta = QtGui.QLineEdit(self.groupBox_scripts_print3D_3)
        self.lineEdit_super_focus_z_delta.setGeometry(QtCore.QRect(500, 40, 113, 21))
        self.lineEdit_super_focus_z_delta.setObjectName(_fromUtf8("lineEdit_super_focus_z_delta"))
        self.label_10 = QtGui.QLabel(self.groupBox_scripts_print3D_3)
        self.label_10.setGeometry(QtCore.QRect(510, 20, 131, 20))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.lineEdit_super_focus_power = QtGui.QLineEdit(self.groupBox_scripts_print3D_3)
        self.lineEdit_super_focus_power.setGeometry(QtCore.QRect(620, 40, 113, 21))
        self.lineEdit_super_focus_power.setObjectName(_fromUtf8("lineEdit_super_focus_power"))
        self.label_11 = QtGui.QLabel(self.groupBox_scripts_print3D_3)
        self.label_11.setGeometry(QtCore.QRect(630, 20, 131, 20))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.lineEdit_super_focus_number = QtGui.QLineEdit(self.groupBox_scripts_print3D_3)
        self.lineEdit_super_focus_number.setGeometry(QtCore.QRect(240, 90, 113, 21))
        self.lineEdit_super_focus_number.setObjectName(_fromUtf8("lineEdit_super_focus_number"))
        self.label_14 = QtGui.QLabel(self.groupBox_scripts_print3D_3)
        self.label_14.setGeometry(QtCore.QRect(370, 70, 131, 20))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.lineEdit_super_focus_spatial = QtGui.QLineEdit(self.groupBox_scripts_print3D_3)
        self.lineEdit_super_focus_spatial.setGeometry(QtCore.QRect(370, 90, 113, 21))
        self.lineEdit_super_focus_spatial.setObjectName(_fromUtf8("lineEdit_super_focus_spatial"))
        self.label_15 = QtGui.QLabel(self.groupBox_scripts_print3D_3)
        self.label_15.setGeometry(QtCore.QRect(240, 70, 111, 20))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.pushButton_super_pause = QtGui.QPushButton(self.tab_scripts)
        self.pushButton_super_pause.setGeometry(QtCore.QRect(40, 450, 121, 41))
        self.pushButton_super_pause.setObjectName(_fromUtf8("pushButton_super_pause"))
        self.pushButton_super_stop = QtGui.QPushButton(self.tab_scripts)
        self.pushButton_super_stop.setGeometry(QtCore.QRect(190, 450, 121, 41))
        self.pushButton_super_stop.setObjectName(_fromUtf8("pushButton_super_stop"))
        self.tabWidget.addTab(self.tab_scripts, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox.setTitle(_translate("MainWindow", "CONTROLLER", None))
        self.pushButton_laser_ctrl_stop.setText(_translate("MainWindow", "STOP", None))
        self.label_zstage_ctrl.setText(_translate("MainWindow", "Z_STAGE_CTRL", None))
        self.label_donor_ctrl.setText(_translate("MainWindow", "DONOR_CTRL", None))
        self.pushButton_donor_ctrl_start.setText(_translate("MainWindow", "START", None))
        self.pushButton_laser_ctrl_start.setText(_translate("MainWindow", "START", None))
        self.pushButton_receiver_ctrl_stop.setText(_translate("MainWindow", "STOP", None))
        self.pushButton_zstage_ctrl_start.setText(_translate("MainWindow", "START", None))
        self.label_reveiver_ctrl.setText(_translate("MainWindow", "RECEIVER_CTRL", None))
        self.pushButton_zstage_ctrl_stop.setText(_translate("MainWindow", "STOP", None))
        self.pushButton_donor_ctrl_stop.setText(_translate("MainWindow", "STOP", None))
        self.pushButton_receiver_ctrl_start.setText(_translate("MainWindow", "START", None))
        self.label_laser_ctrl.setText(_translate("MainWindow", "LASER_CTRL", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_general), _translate("MainWindow", "|  GENERAL  |", None))
        self.groupBox_zstage.setTitle(_translate("MainWindow", "Z STAGE", None))
        self.pushButton_zstage_home.setText(_translate("MainWindow", "HOME", None))
        self.pushButton_zstage_move_rel.setText(_translate("MainWindow", "MOVE_REL [mm]", None))
        self.pushButton_zstage_move_abs.setText(_translate("MainWindow", "MOVE_ABS [mm]", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_z_stage), _translate("MainWindow", "|  Z_STAGE  |", None))
        self.groupBox_donor_x.setTitle(_translate("MainWindow", "DONOR X", None))
        self.pushButton_donor_x_home.setText(_translate("MainWindow", "HOME", None))
        self.pushButton_donor_x_move_rel.setText(_translate("MainWindow", "MOVE_REL [mm]", None))
        self.pushButton_donor_x_move_abs.setText(_translate("MainWindow", "MOVE_ABS [mm]", None))
        self.groupBox_donor_y.setTitle(_translate("MainWindow", "DONOR Y", None))
        self.pushButton_donor_y_home.setText(_translate("MainWindow", "HOME", None))
        self.pushButton_donor_y_move_rel.setText(_translate("MainWindow", "MOVE_REL [mm]", None))
        self.pushButton_donor_y_move_abs.setText(_translate("MainWindow", "MOVE_ABS [mm]", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_donor), _translate("MainWindow", "|  DONOR  |", None))
        self.groupBox_receiver_stepper_x.setTitle(_translate("MainWindow", "RECEIVER X", None))
        self.pushButton_receiver_stepper_x_home.setText(_translate("MainWindow", "HOME", None))
        self.pushButton_receiver_stepper_x_move_rel.setText(_translate("MainWindow", "MOVE_REL [mm]", None))
        self.pushButton_receiver_stepper_x_move_abs.setText(_translate("MainWindow", "MOVE_ABS [mm]", None))
        self.groupBox_receiver_stepper_y.setTitle(_translate("MainWindow", "RECEIVER Y", None))
        self.pushButton_receiver_stepper_y_home.setText(_translate("MainWindow", "HOME", None))
        self.pushButton_receiver_stepper_y_move_rel.setText(_translate("MainWindow", "MOVE_REL [mm]", None))
        self.pushButton_receiver_stepper_y_move_abs.setText(_translate("MainWindow", "MOVE_ABS [mm]", None))
        self.groupBox_receiver_stepper_z.setTitle(_translate("MainWindow", "RECEIVER Z", None))
        self.pushButton_receiver_stepper_z_home.setText(_translate("MainWindow", "HOME", None))
        self.pushButton_receiver_stepper_z_move_rel.setText(_translate("MainWindow", "MOVE_REL [mm]", None))
        self.pushButton_receiver_stepper_z_move_abs.setText(_translate("MainWindow", "MOVE_ABS [mm]", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_receiver_stepper), _translate("MainWindow", "|  RECEIVER  |", None))
        self.groupBox_laser.setTitle(_translate("MainWindow", "LASER", None))
        self.pushButton_laser_power.setText(_translate("MainWindow", "SET POWER [%]", None))
        self.pushButton_laser_singlePulse.setText(_translate("MainWindow", "SINGLE PULSE", None))
        self.pushButton_laser_multiPulse.setText(_translate("MainWindow", "MULTI PULSE [#]", None))
        self.pushButton_laser_on.setText(_translate("MainWindow", "LASER ON", None))
        self.pushButton_laser_off.setText(_translate("MainWindow", "LASER OFF", None))
        self.label.setText(_translate("MainWindow", "POWER SETPOINT", None))
        self.label_2.setText(_translate("MainWindow", "NUMBER OF PULSES", None))
        self.label_3.setText(_translate("MainWindow", "POWER", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_laser), _translate("MainWindow", "| LASER |", None))
        self.groupBox_scripts_print3D.setTitle(_translate("MainWindow", "PRINT 3D", None))
        self.pushButton_super_print3D.setText(_translate("MainWindow", "START", None))
        self.lineEdit_super_print3D_laserPower.setText(_translate("MainWindow", "0.0", None))
        self.label_4.setText(_translate("MainWindow", "LASER POWER", None))
        self.groupBox_scripts_print3D_2.setTitle(_translate("MainWindow", "ENERGY SCAN", None))
        self.pushButton_super_energy.setText(_translate("MainWindow", "START", None))
        self.label_5.setText(_translate("MainWindow", "LASER POWER MIN", None))
        self.lineEdit_super_energy_laser_min.setText(_translate("MainWindow", "0.0", None))
        self.lineEdit_super_energy_laser_max.setText(_translate("MainWindow", "100.0", None))
        self.label_6.setText(_translate("MainWindow", "LASER POWER MAX", None))
        self.lineEdit_super_energy_laser_delta.setText(_translate("MainWindow", "10.0", None))
        self.label_7.setText(_translate("MainWindow", "LASER POWER DELTA", None))
        self.label_12.setText(_translate("MainWindow", "NUMBER OF STEPS", None))
        self.lineEdit_super_energy_number.setText(_translate("MainWindow", "10", None))
        self.label_13.setText(_translate("MainWindow", "SPATIAL SEPARATION", None))
        self.lineEdit_super_energy_spatial.setText(_translate("MainWindow", "0.05", None))
        self.groupBox_scripts_print3D_3.setTitle(_translate("MainWindow", "FOCUS SCAN", None))
        self.pushButton_super_focus.setText(_translate("MainWindow", "START", None))
        self.label_8.setText(_translate("MainWindow", "Z_STAGE MIN", None))
        self.lineEdit_super_focus_z_min.setText(_translate("MainWindow", "0.0", None))
        self.lineEdit_super_focus_z_max.setText(_translate("MainWindow", "10.0", None))
        self.label_9.setText(_translate("MainWindow", "Z_STAGE MAX", None))
        self.lineEdit_super_focus_z_delta.setText(_translate("MainWindow", "1.0", None))
        self.label_10.setText(_translate("MainWindow", "Z_STAGE DELTA", None))
        self.lineEdit_super_focus_power.setText(_translate("MainWindow", "20.0", None))
        self.label_11.setText(_translate("MainWindow", "LASER POWER", None))
        self.lineEdit_super_focus_number.setText(_translate("MainWindow", "10", None))
        self.label_14.setText(_translate("MainWindow", "SPATIAL SEPARATION", None))
        self.lineEdit_super_focus_spatial.setText(_translate("MainWindow", "0.05", None))
        self.label_15.setText(_translate("MainWindow", "NUMBER OF STEPS", None))
        self.pushButton_super_pause.setText(_translate("MainWindow", "PAUSE", None))
        self.pushButton_super_stop.setText(_translate("MainWindow", "STOP", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_scripts), _translate("MainWindow", "| SCRIPTS |", None))

