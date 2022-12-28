#!/user/bin/env python3

from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (64, 64)
camera.start_preview()
sleep(5)
camera.stop_preview()
camera.capture('test1.jpg', resize=(4, 4))