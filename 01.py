a = [0,1,2,3,45]
b = a
b[0] = 10
print(a)
print(b)

import RPi.GPIO as GPIO            # import RPi.GPIO module  
from time import sleep             # lets us have a delay  
GPIO.setmode(GPIO.BCM)             # choose BCM or BOARD  
GPIO.setup(23, GPIO.OUT)           # set GPIO24 as an output   
GPIO.setup(24, GPIO.OUT)           # set GPIO24 as an output   

try:
    while True:  
        GPIO.output(23, 1)         # set GPIO24 to 1/GPIO.HIGH/True  
        sleep(0.1)
        GPIO.output(23, 0)         # set GPIO24 to 1/GPIO.HIGH/True  
        sleep(0.3)
        GPIO.output(23, 1)         # set GPIO24 to 1/GPIO.HIGH/True  
        sleep(0.1)
        GPIO.output(23, 0)         # set GPIO24 to 1/GPIO.HIGH/True  
        sleep(0.3)

        GPIO.output(24, 1)         # set GPIO24 to 1/GPIO.HIGH/True  
        print('set on')
        sleep(0.1)                 # wait half a second  
        GPIO.output(24, 0)         # set GPIO24 to 1/GPIO.HIGH/True  
        print('set OFF')
        sleep(0.5)                 # wait half a second  

        GPIO.output(24, 1)         # set GPIO24 to 1/GPIO.HIGH/True  
        sleep(0.1)                 # wait half a second  
        GPIO.output(24, 0)         # set GPIO24 to 1/GPIO.HIGH/True  
        sleep(0.1)                 # wait half a second  
        GPIO.output(24, 1)         # set GPIO24 to 1/GPIO.HIGH/True  
        sleep(0.1)                 # wait half a second  
        GPIO.output(24, 0)         # set GPIO24 to 1/GPIO.HIGH/True  
        sleep(0.1)                 # wait half a second  
        GPIO.output(24, 1)         # set GPIO24 to 1/GPIO.HIGH/True  
        sleep(0.1)                 # wait half a second  
        GPIO.output(24, 0)         # set GPIO24 to 1/GPIO.HIGH/True          sleep(0.1)                 # wait half a second  
        sleep(0.1)                 # wait half a second  
        GPIO.output(23, 1)         # set GPIO24 to 1/GPIO.HIGH/True  
        sleep(0.1)                 # wait half a second  
        GPIO.output(23, 0)         # set GPIO24 to 1/GPIO.HIGH/True  
        sleep(0.1)                 # wait half a second  
        GPIO.output(23, 1)         # set GPIO24 to 1/GPIO.HIGH/True  
        sleep(0.1)                 # wait half a second  
        GPIO.output(23, 0)         # set GPIO24 to 1/GPIO.HIGH/True  
        sleep(0.1)                 # wait half a second  
        GPIO.output(23, 1)         # set GPIO24 to 1/GPIO.HIGH/True  
        sleep(0.1)                 # wait half a second  
        GPIO.output(23, 0)         # set GPIO24 to 1/GPIO.HIGH/True  
        sleep(0.1)                 # wait half a second  
        GPIO.output(24, 1)         # set GPIO24 to 1/GPIO.HIGH/True  
        sleep(0.1)                 # wait half a second  
        GPIO.output(24, 0)         # set GPIO24 to 1/GPIO.HIGH/True  
        sleep(0.1)                 # wait half a second  
        GPIO.output(24, 1)         # set GPIO24 to 1/GPIO.HIGH/True  
        sleep(0.1)                 # wait half a second  
        GPIO.output(24, 0)         # set GPIO24 to 1/GPIO.HIGH/True  
        sleep(0.1)                 # wait half a second  
        GPIO.output(24, 1)         # set GPIO24 to 1/GPIO.HIGH/True  
        sleep(0.1)                 # wait half a second  
        GPIO.output(24, 0)         # set GPIO24 to 1/GPIO.HIGH/True  
        sleep(0.1)                 # wait half a second  
        GPIO.output(24, 1)         # set GPIO24 to 1/GPIO.HIGH/True  
        sleep(0.1)                 # wait half a second  
        GPIO.output(24, 0)         # set GPIO24 to 1/GPIO.HIGH/True  
  
except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt  
    GPIO.cleanup()                 # resets all GPIO ports used by this program  

