import time
import board
import touchio
import neopixel

touch_pad = touchio.TouchIn(board.A1)

num_pixels = 10  
pixels = neopixel.NeoPixel(board.NEOPIXEL, num_pixels)
pixels.brightness = 0.5

while True:
    if touch_pad.value:
        pixels.fill((255, 255, 255))
    else:
        pixels.fill((0, 0, 0))
    
    time.sleep(0.1) 
