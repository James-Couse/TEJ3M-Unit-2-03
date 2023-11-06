"""
Created by: James Couse
Created on: Oct 23 2023
This module turns the builtin LED on and off.
"""

import time
import board
import digitalio

led = digitalio.DigitalInOut(board.GP9)

led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(1)
    led.value = False
    time.sleep(1)
