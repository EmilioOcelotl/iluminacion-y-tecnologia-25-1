import board
import touchio
import neopixel
import time

# Configuración de los pines de tacto capacitivo
touch_A1 = touchio.TouchIn(board.A1)
touch_A2 = touchio.TouchIn(board.A2)

# Configuración de los LEDs integrados
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.5, auto_write=False)

# El color inicial para las transiciones
current_color = [0, 0, 0]

# Función para suavizar la transición de color en los LEDs
def color_transition(start_color, end_color, steps=50, delay=0.01):
    for i in range(steps):
        r = start_color[0] + (end_color[0] - start_color[0]) * i // steps
        g = start_color[1] + (end_color[1] - start_color[1]) * i // steps
        b = start_color[2] + (end_color[2] - start_color[2]) * i // steps
        pixels.fill((r, g, b))
        pixels.show()
        time.sleep(delay)
    return end_color

while True:
    if touch_A1.value:
        current_color = color_transition(current_color, [255, 0, 0])  # Rojo
        current_color = color_transition(current_color, [0, 0, 0])  # Apagar LEDs
        pixels.fill((0, 0, 0))  # Asegura que los LEDs estén completamente apagados
        pixels.show()

    if touch_A2.value:
        current_color = color_transition(current_color, [0, 0, 255])  # Azul
        current_color = color_transition(current_color, [0, 0, 0])  # Apagar LEDs
        pixels.fill((0, 0, 0))  # Asegura que los LEDs estén completamente apagados
        pixels.show()
