#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

beepPin = 11

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(beepPin, GPIO.OUT)
    GPIO.output(beepPin, GPIO.HIGH)

def loop():
    while True:
        GPIO.output(beepPin, GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(beepPin, GPIO.HIGH)
        time.sleep(0.1)

def destroy():
    GPIO.output(beepPin, GPIO.HIGH)
    GPIO.cleanup()

if __name__ == '__main__':
    print 'Press Ctrl+C to end the program.'
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()


