
import time
from adafruit_circuitplayground.express import cpx

cpx.detect_taps = 2

while True:
    if cpx.tapped:
        print("Double Tapped!")
    time.sleep(0.05)