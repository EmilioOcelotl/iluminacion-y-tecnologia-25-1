from adafruit_circuitplayground.express import cpx
import time
import board
import digitalio

led_pin = digitalio.DigitalInOut(board.A1)
led_pin.direction = digitalio.Direction.OUTPUT

# Loop principal
while True:
    if cpx.button_a:  
        led_pin.value = True  
    elif cpx.button_b:  
        led_pin.value = False  
    
    time.sleep(0.1)  
