import time

import board
from digitalio import DigitalInOut, Direction
# digital LEDs connected on A1

digital_leds = DigitalInOut(board.A1)
digital_leds.direction = Direction.OUTPUT
while True:
    digital_leds.value = True
    time.sleep(.5)
    digital_leds.value = False
    time.sleep(.5)
