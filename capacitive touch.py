from adafruit_circuitplayground import cpx

cpx.adjust_touch_threshold(200)

while True:
    if cpx.touch_A1:
        print('Touched pad A1')