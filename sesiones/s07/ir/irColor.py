# Código para recibir un mensaje de un control remoto o de otra CPX 
# Es necesario cambiar el número más abajo

import pulseio
import board
import adafruit_irremote
import neopixel
import time

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.3, auto_write=False)

pulsein = pulseio.PulseIn(board.IR_RX, maxlen=120, idle_state=True)

decoder = adafruit_irremote.GenericDecode()

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
current_color_index = 0  

def change_color():
    global current_color_index
    pixels.fill(colors[current_color_index])
    pixels.show()
    current_color_index = (current_color_index + 1) % len(colors)

while True:
    pulses = decoder.read_pulses(pulsein)
    try:
        received_code = decoder.decode_bits(pulses)
    except adafruit_irremote.IRNECRepeatException:
        continue
    except adafruit_irremote.IRDecodeException as e:
        continue

    print("Código infrarrojo NEC recibido: ", received_code)

    if received_code == (24, 231, 16, 239): # Cambiar código dependiendo del dispositivo 
        print("Recibido código (0, 0), cambiando color")
        change_color()

    time.sleep(0.1)  