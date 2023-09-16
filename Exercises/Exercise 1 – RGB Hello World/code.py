# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
# SPDX-License-Identifier: MIT

# Aalya Sharaf – Assignment 1
# RGB Hello World
# Recreating a traffic light (green light, blinking green light, yellow light, and red light)

"""CircuitPython Essentials Internal RGB LED red, green, blue example"""
import time
import board

if hasattr(board, "APA102_SCK"):
    import adafruit_dotstar

    led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
else:
    import neopixel

    led = neopixel.NeoPixel(board.NEOPIXEL, 1)

led.brightness = 0.3

while True:
    # Start with a green light
    led[0] = (0, 255, 0)
    time.sleep(6.0)
    
    # Make the green light blink
    for _ in range(6):
        led[0] = (0, 255, 0)  # Turn off
        time.sleep(0.5)
        led[0] = (0, 0, 0)  # Turn on
        time.sleep(0.5)
   
    # Turn the light yellow
    led[0] = (255, 255, 0)
    time.sleep(3.0)
    
    # Turn the light Red
    led[0] = (255, 0, 0)
    time.sleep(10.0)