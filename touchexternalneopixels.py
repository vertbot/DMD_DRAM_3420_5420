from adafruit_circuitplayground.express import cpx
import time
import neopixel
import board
import random

pixel_pin = board.A3
pixel_pin_strip = board.A5

num_pixels = 2
num_pixels_strip = 30

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3)
pixels_strip = neopixel.NeoPixel(pixel_pin_strip, num_pixels_strip, brightness=0.3)

cpx.adjust_touch_threshold(200)
cpx.pixels.brightness = 0.3

red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
purple = (76, 0, 153)
orange = (255, 128, 0)
black = (0, 0, 0)

random_color_list = (red, green, blue, purple, orange)


while True:
    if cpx.touch_A1:
        #pixels.fill(red)
        pixels[0] = blue
        pixels[1] = green
        
        for i in range(30):
            pixels_strip[i] = random.choice(random_color_list)
            time.sleep(.2)
    else:
        pixels.fill(black)
        pixels_strip.fill(black)

