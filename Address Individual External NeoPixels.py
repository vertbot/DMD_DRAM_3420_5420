import time
import board
import neopixel

pixel_pin = board.A1
num_pixels = 3

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)
#items with commas like this are lists (actually a tuple, which are unmutable lists.)
BLUE = (0, 0, 255)
RED = (255, 0, 0) 
GREEN = (0,128,0)
while True:
    #[] represents a list. 
    pixels[0] = (RED) #[0] represents an item in a list, in this case item zero.
    pixels[1] = (BLUE)
    pixels[2] = (GREEN)
    pixels.show()  
    time.sleep(1)
    pixels[0] = (BLUE) 
    pixels[1] = (GREEN)
    pixels[2] = (RED)    
    pixels.show()  
    time.sleep(1) 
