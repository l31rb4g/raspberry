#!/usr/bin/python
import sys
import RPi.GPIO as GPIO
from time import sleep

channels = {
    '1': 18,
    '2': 16,
    '3': 15,
    '4': 13
}

if len(sys.argv) == 3:
    c = int(sys.argv[1])
    print('channel ' + str(c))
    status = sys.argv[2]

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(c, GPIO.OUT)

    if status == 'on':
        GPIO.output(c, GPIO.LOW)
    elif status == 'off':
        GPIO.output(c, GPIO.HIGH)
