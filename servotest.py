# Code by Jason Yoddumnern
# allowed for reuse blah blah blah
# Last Updated 2019 March 18
# 
# Code to control Servo HAT utilising up to 16 channels

import time
from adafruit_servokit import ServoKit

# Kit used: servo HAT
kit = ServoKit(channels=16)

kit.servo[0].angle = 180
time.sleep(3)

kit.servo[0].angle = 0
time.sleep(3)

kit.servo[0].angle = 180
time.sleep(3)

kit.servo[0].angle = 0
time.sleep(3)

