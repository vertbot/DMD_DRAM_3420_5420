from adafruit_circuitplayground.express import cpx
import time
cpx.adjust_touch_threshold(200)
cpx.pixels.brightness = 0.3

red = (255, 0, 0)
blue = (0,0,255)
green = (0,255,0)
black = (0,0,0)

while True:
    if cpx.touch_A1:
        for i in range(10):
            cpx.pixels[i] = red
            time.sleep(.2)
            cpx.pixels[i] = green
            time.sleep(.2)
            cpx.pixels[i] = blue
            time.sleep(.2)
    else:
        cpx.pixels.fill(black)