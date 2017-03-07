#!/usr/bin/env python
#onionGpio appears to be python2 only

import time
import onionGpio

onVal = 0
offVal = 1

# Blue
BLUE_LED = 15
gpioObjBlue = onionGpio.OnionGpio(BLUE_LED)
status  = gpioObjBlue.setOutputDirection(0)
status  = gpioObjBlue.setValue(offVal)
#time.sleep(0.2)

# Green
GREEN_LED = 16
gpioObjGreen = onionGpio.OnionGpio(GREEN_LED)
status  = gpioObjGreen.setOutputDirection(0)
status  = gpioObjGreen.setValue(offVal)
#time.sleep(0.2)

# Red
RED_LED = 17
gpioObjRed = onionGpio.OnionGpio(RED_LED)
status  = gpioObjRed.setOutputDirection(0)
status  = gpioObjRed.setValue(offVal)
#time.sleep(0.2)

# Sequence (in theory) Blue, Green, Cyan, Red, Magenta, Yellow, White.
# However, you would have to adjust the duty values to approach Yellow
# or White.
# If you make a small cylinder of paper about the diameter of a pencil and
# the same height and place it over the led, you get better looking colors.
loop    = True
try:
    while loop:
        for value in range(1,8):
            if value&1:
                status = gpioObjBlue.setValue(onVal)
            else:
                status = gpioObjBlue.setValue(offVal)
            if value&2:
                status = gpioObjGreen.setValue(onVal)
            else:
                status = gpioObjGreen.setValue(offVal)
            if value&4:
                status = gpioObjRed.setValue(onVal)
            else:
                status = gpioObjRed.setValue(offVal)

            time.sleep(1)

except KeyboardInterrupt:
    status = gpioObjBlue.setValue(offVal)
    status = gpioObjGreen.setValue(offVal)
    status = gpioObjRed.setValue(offVal)
    print("Exiting")
"blink_each.py" 59L, 1634C
