from time import monotonic as now
from adafruit_circuitplayground.express import cpx
# https://www.youtube.com/watch?v=Rl5EqPiOwsU
cpx.pixels.brightness = 0.3
Black = (0, 0, 0)
Blue = (0, 0, 255)
Red = (255, 0, 0)
numberofblinks = 0

def var_sleep(delay):
    start = now()
    while start + delay > now():
        yield

def letgo():
    yield
    cpx.play_file("siren.wav")

def popo_animation():
    if cpx.button_a or cpx.touch_A1:
        yield
        for foo in range(6):
            for i in range(5):
                cpx.pixels[i] = Red
            for i in range(5):
                cpx.pixels[5+i] = Blue
            yield from var_sleep(.5)
            for i in range(5):
                cpx.pixels[i] = Blue
            for i in range(5):
                cpx.pixels[5+i] = Red
            yield from var_sleep(.5)
        cpx.pixels.fill(Black)
while True:
    letgo()
    popo_animation()
