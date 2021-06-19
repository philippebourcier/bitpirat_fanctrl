# bitpirat_fanctrl

EMC2301 & EMC2302 PID fan controller for BitPiRat Gen1 board & Co

The only fans tested with this code are Noctua's NF-A8 (12V) and NF-A4x20 (5V or 12V).
Different brands of fans will have different settings...
The 4 Pin PWM Fan header doesn't specify a voltage.
You can find 5V, 12V and 24V fans running on 4 Pin PWM... thus you will have to check carefully what is the right voltage for your board.
BitPiRat and Waveshare uses a 5V fan.
Official Raspberry Pi Compute Module 4 IO Board uses a 12V fan.
Noctua's NF-A4x20 PWM exists in both 12V and 5V variants.
Noctua (Austria) is probably the best PC fan brand in the world... you might want to try something else, but you'll have to recreate the /path/to/bitpirat_fanctrl/i2c_pkg/emc2301_pkg/fan_type.py file... which doesn't look like something fun.

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

Or you could use Waveshare's code, which is very basic and requires a bit of tuning, though...
https://www.waveshare.com/wiki/CM4-IO-BASE-B

Original Python EMC2301 code from :
https://github.com/mamin27/ecomet_i2c_raspberry_tools/tree/master/i2c_pkg/emc2301_pkg
(Thus this code is GPLv3 and not BSD, sorry...)

PID Implementation from :
https://onion.io/2bt-pid-control-python/

