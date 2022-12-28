#!/usr/bin/env python3

import signal
import sys
import time
import RPi.GPIO as GPIO

GPIO_LED = 4

if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_LED, GPIO.OUT, initial=GPIO.LOW)

    GPIO.output(GPIO_LED, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(GPIO_LED, GPIO.LOW)
    
    GPIO.cleanup()
    sys.exit(0)