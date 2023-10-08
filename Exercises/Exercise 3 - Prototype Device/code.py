import time
import board
import analogio
import digitalio
import neopixel

# Set the pin for the LDR
ldr_pin = analogio.AnalogIn(board.A1)

# Set the pin for the NeoPixel ring
pixel_pin = board.D5
num_pixels = 12

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2)

# LDR threshold
threshold = 40000

print("Enabling NeoPixel power!")
enable = digitalio.DigitalInOut(board.D10)
enable.direction = digitalio.Direction.OUTPUT
enable.value = True

# Creating a loop that constantly checks conditions.
while True:
    ldr_value = ldr_pin.value
    print("LDR Value:", ldr_value)

    # if LDR value is less that threshold – turn on light! Else, Light is off. 
    if ldr_value < threshold:
        pixels.fill((255, 0, 0))
    else:
        pixels.fill((0, 0, 0))

    pixels.show() 
    time.sleep(0.5)  # Half-second delay
