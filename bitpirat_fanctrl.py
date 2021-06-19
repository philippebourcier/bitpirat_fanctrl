#!/usr/bin/env python3

# wget https://raw.githubusercontent.com/ivmech/ivPID/master/PID.py
import PID
# pip3 install daemonize
from daemonize import Daemonize
# argv
from sys import argv

# sleep
from time import sleep

# emc2301 from https://github.com/mamin27/ecomet_i2c_raspberry_tools/tree/master/i2c_pkg/emc2301_pkg
from  i2c_pkg.emc2301_pkg import emc2301

# functions
def clamp(n,minn,maxn):
    return max(min(maxn,n),minn)

def fanctrl(mode=''):

    sens = emc2301.EMC2301()

    # ARE WE ALL GOOD ?
    ret = sens.self_test()
    if ret != 0 :
        print("Not a RasPi ? / Not a BitPiRat ?")
        exit()

    # CHECK TEMP AND ADAPT FAN SPEED
    # target temperature is 34°C 
    targetT = 34
    # number of seconds between measures & fan speed update
    updateInterval=5
    # PID settings
    P = 30.
    I = 1.
    D = 1.
    # init
    temperature=0

    pid = PID.PID(P,I,D)
    pid.SetPoint = targetT
    pid.setSampleTime(updateInterval)
    pid.SetPoint = targetT
    pid.setKp(P)
    pid.setKi(I)
    pid.setKd(D)

    while True:

        # read temperature
        with open('/sys/class/hwmon/hwmon0/temp1_input') as t: temperature=float(t.read())/1000
        pid.update(temperature)
        targetSpeed = int(clamp(abs(pid.output),0,255))

        # debug
        if(mode=="debug"):
            print(temperature)
            print(targetSpeed)
            print("**********")

        # set FAN speed
        sens.write_register(register='FAN_SETTING',value=targetSpeed)
        sleep(updateInterval)

if len(argv)==2 and argv[1]=="-d":
    daemon = Daemonize(app="bitpirat_fanctrl",pid="/run/bitpirat_fanctrl.pid",action=fanctrl)
    daemon.start()
else:
    fanctrl("debug")

