import time
import board
from digitalio import DigitalInOut, Direction, Pull

coil1 = DigitalInOut(board.A1)
coil2 = DigitalInOut(board.A2)
coil3 = DigitalInOut(board.A3)
coil4 = DigitalInOut(board.A4)

coil1.direction = Direction.OUTPUT
coil2.direction = Direction.OUTPUT
coil3.direction = Direction.OUTPUT
coil4.direction = Direction.OUTPUT

# Configuración de los botones A y B
button_a = DigitalInOut(board.BUTTON_A)
button_a.direction = Direction.INPUT
button_a.pull = Pull.DOWN

button_b = DigitalInOut(board.BUTTON_B)
button_b.direction = Direction.INPUT
button_b.pull = Pull.DOWN

steps = [
    [1, 0, 0, 1],  # Paso 1
    [1, 0, 0, 0],  # Paso 2
    [1, 1, 0, 0],  # Paso 3
    [0, 1, 0, 0],  # Paso 4
    [0, 1, 1, 0],  # Paso 5
    [0, 0, 1, 0],  # Paso 6
    [0, 0, 1, 1],  # Paso 7
    [0, 0, 0, 1],  # Paso 8
]

def set_step(coil1_val, coil2_val, coil3_val, coil4_val):
    coil1.value = coil1_val
    coil2.value = coil2_val
    coil3.value = coil3_val
    coil4.value = coil4_val

def rotate_motor(direction, delay=0.01):
    for step in (steps if direction == 1 else reversed(steps)):
        set_step(*step)
        time.sleep(delay)

while True:
    if button_a.value:  # Si el botón A está presionado, mueve a la izquierda
        rotate_motor(-1)  # Gira en dirección inversa
    elif button_b.value:  # Si el botón B está presionado, mueve a la derecha
        rotate_motor(1)  # Gira en dirección normal
    else:
        set_step(0, 0, 0, 0)  # Apaga todas las bobinas para detener el motor

    time.sleep(0.01) 
