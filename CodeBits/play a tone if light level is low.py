import time
from adafruit_circuitplayground.express import cpx

while True:
    if cpx.light < 30:
        cpx.play_tone(400, 1.0)  # 440 hx for 1 second
    print("Light Value:", cpx.light)
    time.sleep(1)