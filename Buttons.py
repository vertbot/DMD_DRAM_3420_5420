import time
from adafruit_circuitplayground.express import cpx

while True:
    if cpx.button_a:
        print("button A was pressed")
        time.sleep(1)
    elif cpx.button_b:
        print("button B was pressed")
        time.sleep(1)
