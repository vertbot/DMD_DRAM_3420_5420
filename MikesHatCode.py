import time
import board
import adafruit_hcsr04
import neopixel
import random
from adafruit_circuitplayground.express import cpx
from rainbowio import colorwheel


sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.A6, echo_pin=board.A1)
pixel_pin = board.A3
pixel_pin2 = board.A2

num_pixels = 6

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=2, auto_write=False)
pixels2 = neopixel.NeoPixel(pixel_pin2, 1, brightness=.1, auto_write=False)

red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255, 150, 0)
cyan = (0, 255, 255)
purple = (76, 0, 153)
orange = (255, 128, 0)
black = (0, 0, 0)
random_color_list = (green, blue, purple, orange)

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = colorwheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)
def randomcolor():
    for i in range(6):
        pixels[i] = random.choice(random_color_list)
        time.sleep(.1)
        pixels.show()
        
def alertnotification():
    pixels.fill(red)
    pixels.show()
    pixels2.fill(red)
    pixels2.show()
    time.sleep(1)
    
def clearpixels():
    pixels2.fill(black)
    pixels2.show()
    pixels.fill(black)
    pixels.show()
    
buttonpress = 'c'   
alert = False
while True:
    if cpx.button_a:
        buttonpress = 'a'
    elif cpx.button_b:
        buttonpress = 'b'    

    if cpx.switch is True:
        buttonpress = 'c'   
    elif buttonpress == 'a':
        rainbow_cycle(0)
    elif buttonpress == 'b':
        randomcolor()
    elif buttonpress == 'c':
        clearpixels()
    try:
        # print((sonar.distance,))
        if sonar.distance <= 90:
            alert = True
            time.sleep(.2)
        elif sonar.distance > 90:
            alert = False
            pixels2.fill(black)
            pixels2.show()
    except RuntimeError:
        print("Retrying!")
    if alert is True:
        alertnotification()
       
    time.sleep(0.1)    
    # print(buttonpress)
    # print(alert)
