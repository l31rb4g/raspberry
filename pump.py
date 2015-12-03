#!/usr/bin/python
#encoding: utf-8
import sys
import RPi.GPIO as GPIO
from time import sleep

class Pump:

    channels = {
        '1': 18,
        '2': 16,
        '3': 15,
        '4': 13
    }

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)

        c = False

        if len(sys.argv) > 1:
            n = sys.argv[1]
            if int(n) >= 1 and int(n) <= 4:
                c = self.channels[sys.argv[1]]
            else:
                print('Canal invalido: ' + n)
        else:
            print('Digite o número do canal')

        if c:
            try:
                GPIO.setup(c, GPIO.OUT)
                while True:
                    self.wait(80, 'Enchendo')
                    GPIO.output(c, GPIO.LOW)
                    self.wait(200, 'Esvaziando')
                    GPIO.output(c, GPIO.HIGH)

            except KeyboardInterrupt:
                GPIO.cleanup()

    def wait(self, n, msg):
        while True:
            sys.stdout.write('\r' + msg + ' ... ' + str(n) + ' ')
            sys.stdout.flush()
            n -= 1
            sleep(1)
            if n == 0:
                break


if __name__ == '__main__':
    Pump()