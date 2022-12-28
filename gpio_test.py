#!/usr/bin/env python3

import signal
import sys
import time
import RPi.GPIO as GPIO

GPIO_LED = 4

def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)

def button_callback(channel):
    print("Button pressed!")

if __name__ == "__main__":
    #Set up pin layout mode
    GPIO.setmode(GPIO.BCM)

    #Set up pin modes
    GPIO.setup(GPIO_LED, GPIO.OUT, pull_up_down = GPIO.PUD_UP)

    GPIO.add_event_detect(BUTTON_GPIO, GPIO.FALLING, callback=button_callback, bouncetime=100)

    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()
    
