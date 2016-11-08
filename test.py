from ctypes import *
import time

bscStepper = cdll.LoadLibrary("Thorlabs//Thorlabs.MotionControl.Benchtop.StepperMotor.dll")
#status6=bscStepper.SBC_Close("70866729")
status0=bscStepper.TLI_BuildDeviceList()
status1=bscStepper.SBC_Open("70866729")
status2=bscStepper.SBC_LoadSettings("70866729")
status3=bscStepper.SBC_StartPolling("70866729",1,c_int(200))
dur=bscStepper.SBC_PollingDuration("70866729",1)
status4=bscStepper.SBC_Home("70866729",1)
time.sleep(15)

status5=bscStepper.SBC_StopPolling("70866729",1)
dur2=bscStepper.SBC_PollingDuration("70866729",1)


time.sleep(1)
status7=bscStepper.SBC_ClearMessageQueue("70866729",1)
status6=bscStepper.SBC_Close("70866729")
#try:
#    
##    status6=bscStepper.SBC_Close("70866729")
#except:
#    print status6