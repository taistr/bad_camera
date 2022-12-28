#!/usr/bin/env python3

import signal
import sys
import time
from picamera import PiCamera
from datetime import datetime
import RPi.GPIO as GPIO

GPIO_BUTTON = 4
PHOTO_RES = 64

def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)

def button_callback(channel):
    current_dt = datetime.now()
    filename = current_dt.strftime("%H_%M_%S_%d%m%Y.jpg")

    print("Picture taken at", current_dt, end='')
    print(" stored as " + filename)

    dir_save = "pictures/" + filename

    camera.capture(dir_save, resize=(PHOTO_RES, PHOTO_RES))

if __name__ == "__main__":
    """SETUP"""
    #Set up pin layout mode
    GPIO.setmode(GPIO.BCM)

    #Set up pin modes
    GPIO.setup(GPIO_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    """CODE"""
    #Instantiate PiCamera class
    camera = PiCamera()

    #Setup button signal falling event
    GPIO.add_event_detect(GPIO_BUTTON, GPIO.FALLING, callback=button_callback, bouncetime=100)

    #Setup SIGINT event
    signal.signal(signal.SIGINT, signal_handler)

    #Set up viewfinder
    camera.resolution = (64, 64)
    camera.start_preview()

    signal.pause()
    
