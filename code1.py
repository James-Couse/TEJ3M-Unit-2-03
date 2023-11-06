"""
Created by: James Couse
Created on: Oct 23 2023
This module turns the builtin LED on and off.
"""

import time
import board
import digitalio

led_red = digitalio.DigitalInOut(board.GP9)
led_green = digitalio.DigitalInOut(board.GP11)
led_blue = digitalio.DigitalInOut(board.GP13)

led_red.direction = digitalio.Direction.OUTPUT
led_green.direction = digitalio.Direction.OUTPUT
led_blue.direction = digitalio.Direction.OUTPUT

while True:
    led_red.value = True
    led_green.value = False
    led_blue.value = False
