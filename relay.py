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

GPIO.setmode(GPIO.BOARD)

c = False

if len(sys.argv) > 1:
    n = sys.argv[1]
    if int(n) >= 1 and int(n) <= 4:
        c = channels[sys.argv[1]]
    else:
        print('Canal invalido: ' + n)
else:
    print('Digite o numero do canal')

if c:
    try:
        GPIO.setup(c, GPIO.OUT)
        GPIO.output(c, GPIO.LOW)
        input()
    
    except KeyboardInterrupt:
        GPIO.cleanup()

