#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep

channels = {
    '1': 18,
    '2': 15,
    '3': 16,
    '4': 13
}

GPIO.setmode(GPIO.BOARD)

try:
    for c in channels:
        GPIO.setup(channels[c], GPIO.OUT)
        GPIO.output(channels[c], GPIO.HIGH)
    
    for c in channels:
        sleep(1)
        GPIO.output(channels[c], GPIO.LOW)
    
    sleep(1)
    GPIO.cleanup()
    
except KeyboardInterrupt:
    GPIO.cleanup()

