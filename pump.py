#!/usr/bin/python
#encoding: utf-8
import re
import sys
import datetime
import RPi.GPIO as GPIO
from time import sleep

class Pump:

    channels = {
        '1': 18,
        '2': 16,
        '3': 15,
        '4': 13
    }

    channel = 3

    time = {
        'full': 80,
        'empty': 200
    }

    silence = False

    def __init__(self):
        c = self.channels[str(self.channel)]

        if len(sys.argv) > 1 and sys.argv[1] == '--silence':
            self.silence = True

        if c:
            GPIO.setmode(GPIO.BOARD)
            try:
                GPIO.setup(c, GPIO.OUT)
                while True:
                    if not self.silence:
                        print('\n>>> Ligando bomba por ' + self.duration(self.time['full']))
                    GPIO.output(c, GPIO.LOW)
                    self.wait(self.time['full'], 'Enchendo')

                    if not self.silence:
                        print('\n>>> Desligando bomba por ' + self.duration(self.time['empty']))
                    GPIO.output(c, GPIO.HIGH)
                    self.wait(self.time['empty'], 'Esvaziando')

            except KeyboardInterrupt:
                if not self.silence:
                    print('\n\n>>> Desligando tudo\n')
                GPIO.cleanup()

    def wait(self, n, msg):
        while True:
            if not self.silence:
                sys.stdout.write('\r' + msg + ' ... ' + self.duration(n) + ' ')
                sys.stdout.flush()
            n -= 1
            sleep(1)
            if n == 0:
                if not self.silence:
                    sys.stdout.write('\r' + (' ' * 20))
                    sys.stdout.flush()
                break

    def duration(self, n):
        r = str(datetime.timedelta(seconds=int(n)))
        r = re.sub('^0:', '', r)
        return r


if __name__ == '__main__':
    Pump()
