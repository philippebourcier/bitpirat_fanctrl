# bitpirat_fanctrl
EMC2302 fan controller for BitPiRat Gen1 board

```
# cat /etc/rc.local
#!/bin/bash
/root/bitpirat_fanctrl/bitpirat_fanctrl.py -d
```

This code will work on Mirko electronics BitPiRat, as is.
Should you want to make it work on the Waveshare CM4-IO-BASE-B, you only need to do this :
```
wget -O/root/bitpirat_fanctrl/i2c_pkg/emc2301_pkg/emc2301_constant.py https://raw.githubusercontent.com/mamin27/ecomet_i2c_raspberry_tools/master/i2c_pkg/emc2301_pkg/emc2301_constant.py
```

Or you could use their code, which requires a bit of tuning, though...
https://www.waveshare.com/wiki/CM4-IO-BASE-B

