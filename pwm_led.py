#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

ledPin = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.output(ledPin, GPIO.LOW)

p = GPIO.PWM(ledPin, 1000)
p.start(0)

try:
    while True:
        for dc in range(0, 101, 4):
            p.ChangeDutyCycle(dc)
            print str(dc)
            time.sleep(0.05)
        time.sleep(1)
        for dc in range(100, -1, -4):
            p.ChangeDutyCycle(dc)
            print str(dc)
            time.sleep(0.05)
        time.sleep(1)

except KeyboardInterrupt:
    p.stop()
    GPIO.output(ledPin, GPIO.HIGH)
    GPIO.cleanup()

