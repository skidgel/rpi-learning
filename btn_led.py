#!/usr/bin/env python

import RPi.GPIO as GPIO

# Pin assignments.
ledPin = 11
btnPin = 12

def setup():
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(ledPin, GPIO.OUT)
  GPIO.setup(btnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.output(ledPin, GPIO.HIGH)

def loop():
  while True:
    if GPIO.input(btnPin) == GPIO.LOW:
      print 'LED on'
      GPIO.output(ledPin, GPIO.LOW)
    else:
      print 'LED off'
      GPIO.output(ledPin, GPIO.HIGH)

def destroy():
  GPIO.output(ledPin, GPIO.HIGH)
  GPIO.cleanup()

if __name__ == '__main__':
  setup()
  try:
    loop()
  except KeyboardInterrupt:
    destroy()

