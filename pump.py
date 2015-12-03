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
    },

    time = {
        'full': 80,
        'empty': 200
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
                    print('>>> Ligando bomba por ' + str(self.time.full) + 'segundos')
                    GPIO.output(c, GPIO.LOW)
                    self.wait(self.time.full, 'Enchendo')

                    print('>>> Desligando bomba por ' + str(self.time.empty) + 'segundos')
                    GPIO.output(c, GPIO.HIGH)
                    self.wait(self.time.empty, 'Esvaziando')

            except KeyboardInterrupt:
                print('\n')
                GPIO.cleanup()

    def wait(self, n, msg):
        while True:
            sys.stdout.write('\r' + msg + ' ... ' + str(n) + ' ')
            sys.stdout.flush()
            n -= 1
            sleep(1)
            if n == 0:
                print('')
                break


print(__name__)
if __name__ == '__main__':
    Pump()
