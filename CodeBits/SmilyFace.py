from adafruit_circuitplayground.express import cpx
import time
import neopixel
import board
pixel_pin = board.A6
num_pixels = 3
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
purple = (76, 0, 153)
orange = (255, 128, 0)
black = (0, 0, 0)
while True:
    pixels.fill(blue)
    if cpx.touch_A2:
        pixels[0] = red
        pixels[1] = red

        time.sleep(1)