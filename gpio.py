#
# script for managing GPIO
#

import RPi.GPIO as GPIO
import time

class GpioManager:

    def __init__(self):
        """to use Raspberry Pi board pin numbers"""
        GPIO.setmode(GPIO.BOARD)

    def blink_pin(self, pin):
        """convenience function to blink an LED on given pin"""
        GPIO.output(pin,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(pin,GPIO.LOW)
        time.sleep(1)
        return

    def set_pin_output(self, pin):
        """set up GPIO output channels"""
        GPIO.setup(pin, GPIO.OUT)

    def cleanup(self):
        GPIO.cleanup() 
