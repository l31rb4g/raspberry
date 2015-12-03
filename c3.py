#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep

channel = 15

GPIO.setmode(GPIO.BOARD)
GPIO.setup(channel, GPIO.OUT)

try:
    while True:
        GPIO.output(channel, GPIO.HIGH)
        sleep(0.5)
        GPIO.output(channel, GPIO.LOW)
        sleep(0.5)

except KeyboardInterrupt:
   GPIO.cleanup()

