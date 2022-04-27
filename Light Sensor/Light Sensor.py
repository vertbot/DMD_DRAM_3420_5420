import time
from adafruit_circuitplayground.express import cpx

while True:
    print("Light Value:", cpx.light)
    time.sleep(1)
