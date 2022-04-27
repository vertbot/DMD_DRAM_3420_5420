import time
import board
import neopixel

pixel_pin = board.A1
num_pixels = 3

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

while True:
    pixels.fill(RED)
    pixels.show()
    time.sleep(1)
    pixels.fill(BLUE)
    pixels.show()
