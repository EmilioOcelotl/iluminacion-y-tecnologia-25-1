import board
import pulseio

# Configura los pines de salida PWM para los colores RGB
red = pulseio.PWMOut(board.A1, frequency=5000, duty_cycle=0)
green = pulseio.PWMOut(board.A2, frequency=5000, duty_cycle=0)
blue = pulseio.PWMOut(board.A3, frequency=5000, duty_cycle=0)

def set_color(r, g, b):
    # Convierte los valores de 0-255 a 0-65535 para PWM
    red.duty_cycle = int(r * 65535 / 255)
    green.duty_cycle = int(g * 65535 / 255)
    blue.duty_cycle = int(b * 65535 / 255)

# Ejemplo: Cambia el color a rojo
set_color(255, 0, 0)

# Puedes cambiar el color según necesites
# set_color(0, 255, 0) # verde
# set_color(0, 0, 255) # azul