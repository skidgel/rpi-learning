#!/usr/bin/env python

"""LED and GPIO example."""

import RPi.GPIO as GPIO
import time

# Use GPIO pin 11.
ledPin = 11

# Numbers GPIOs by physical location.
GPIO.setmode(GPIO.BOARD)

# Set ledPin mode as output.
GPIO.setup(ledPin, GPIO.OUT)

# Set the ledPin as high (+3.3v) to turn off the led.
GPIO.output(ledPin, GPIO.HIGH)

try:
    while True:
        print '...LED on'
        GPIO.output(ledPin, GPIO.LOW)
        time.sleep(0.5)
        print 'LED off...'
        GPIO.output(ledPin, GPIO.HIGH)
        time.sleep(1)
# Press Ctrl+C to turn off the LED and release the GPIO.
except KeyboardInterrupt:
    GPIO.output(ledPin, GPIO.HIGH)
    GPIO.cleanup()


