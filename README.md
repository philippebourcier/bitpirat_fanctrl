# bitpirat_fanctrl

EMC2301 & EMC2302 PID fan controller for BitPiRat Gen1 board & Co

```
# cat /etc/rc.local
#!/bin/bash
/path/to/bitpirat_fanctrl/bitpirat_fanctrl.py -d
```

Settings you can play with :
- The target temperature, of course :
  targetT = 34
- The number of seconds between measures & fan speed update
  updateInterval=5
- The PID settings
    P = 30.
    I = 1.
    D = 1.

This code will work on Mirko electronics BitPiRat, as is.

Should you want to make it work on the Waveshare CM4-IO-BASE-B or the Official Raspberry Pi Compute Module 4 IO Board, you only need to do this :
```
wget -O/path/to/bitpirat_fanctrl/i2c_pkg/emc2301_pkg/emc2301_constant.py https://raw.githubusercontent.com/mamin27/ecomet_i2c_raspberry_tools/master/i2c_pkg/emc2301_pkg/emc2301_constant.py
```

Or you could use their code, which requires a bit of tuning, though...
https://www.waveshare.com/wiki/CM4-IO-BASE-B

Original Python EMC2301 code from :
https://github.com/mamin27/ecomet_i2c_raspberry_tools/tree/master/i2c_pkg/emc2301_pkg
(https://onion.io/2bt-pid-control-python/)

PID Implementation from :
https://onion.io/2bt-pid-control-python/

