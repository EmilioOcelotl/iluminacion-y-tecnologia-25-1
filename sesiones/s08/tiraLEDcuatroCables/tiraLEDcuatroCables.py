import time
import board
import digitalio

red_pin = digitalio.DigitalInOut(board.A1)   # Rojo
green_pin = digitalio.DigitalInOut(board.A2) # Verde
blue_pin = digitalio.DigitalInOut(board.A3)  # Azul

red_pin.direction = digitalio.Direction.OUTPUT
green_pin.direction = digitalio.Direction.OUTPUT
blue_pin.direction = digitalio.Direction.OUTPUT

red_pin.value = False
green_pin.value = False
blue_pin.value = False

# Definir colores
colors = [
    (1, 0, 0),   # Rojo
    (0, 1, 0),   # Verde
    (0, 0, 1),   # Azul
    (1, 1, 0),   # Amarillo
    (0, 1, 1),   # Cyan
    (1, 0, 1),   # Magenta
    (0, 0, 0),   # Apagar
]

# Inicializar los botones
button_a = digitalio.DigitalInOut(board.BUTTON_A)
button_a.switch_to_input(pull=digitalio.Pull.DOWN)

button_b = digitalio.DigitalInOut(board.BUTTON_B)
button_b.switch_to_input(pull=digitalio.Pull.DOWN)

def set_color(red, green, blue):
    red_pin.value = red
    green_pin.value = green
    blue_pin.value = blue

current_color = 0

try:
    while True:
        if button_a.value:
            current_color = (current_color + 1) % len(colors)
            set_color(*colors[current_color])
            time.sleep(0.3)  

        if button_b.value:
            current_color = (current_color - 1) % len(colors)
            set_color(*colors[current_color])
            time.sleep(0.3)  

except KeyboardInterrupt:
    set_color(0, 0, 0) 
