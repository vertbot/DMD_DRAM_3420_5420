import time
from adafruit_circuitplayground.express import cpx

while True:
    print("Slide Switch:", cpx.switch)
    time.sleep(1)
