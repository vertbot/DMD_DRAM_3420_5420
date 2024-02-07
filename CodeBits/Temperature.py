import time
from adafruit_circuitplayground.express import cpx

while True:
    temperature_c = cpx.temperature
    temperature_f = cpx.temperature * 1.8 +32
    print ("Temperature in Celsius:", temperature_c)
    print ("Temperature in Fahrenheit:", temperature_f)
    time.sleep(1)

# With round or int
#  temperature_f = round(cpx.temperature * 1.8 + 32, 1)
#  temperature_f = int(cpx.temperature * 1.8 + 32)



