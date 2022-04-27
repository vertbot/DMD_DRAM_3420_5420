import time
import board
import neopixel


pixel_pin = board.A1
num_pixels = 23

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1, auto_write=False)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
DRED = (255, 0, 270)

# List of pixel numbers
inner = [1, 5, 7, 8, 9]
outer = [17, 18, 20, 22]
foo = 0

while True:
    #pixels.fill(BLACK)
    #pixels.show()
    if foo == 0:
        for x in inner:
            pixels[x] = RED
            pixels.show()
        for y in outer:
            pixels[y] = DRED
            pixels.show()
        time.sleep(1)
        foo = 1
    else:
        for x in inner:
            pixels[x] = DRED
            pixels.show()
        for y in outer:
            pixels[y] = RED
            pixels.show()
        foo = 0
        time.sleep(1)
        
    print(foo)
