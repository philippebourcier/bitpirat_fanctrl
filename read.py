#!/usr/bin/env python3

# emc2301 from https://github.com/mamin27/ecomet_i2c_raspberry_tools/tree/master/i2c_pkg/emc2301_pkg
from  i2c_pkg.emc2301_pkg import emc2301
sens = emc2301.EMC2301()

# ARE WE ALL GOOD ?
ret = sens.self_test()
if ret != 0 :
    print("Not a RasPi ? / Not a BitPiRat ?")
    exit()

print(sens.speed()[0])
print(sens.read_register(register='FAN_SETTING')[0])
