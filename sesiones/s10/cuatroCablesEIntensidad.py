import time
import board
import pwmio
import digitalio

# Configurar pines de salida con PWM para controlar la intensidad de los LEDs
red_pin = pwmio.PWMOut(board.A1, frequency=5000, duty_cycle=0)   # Rojo
green_pin = pwmio.PWMOut(board.A2, frequency=5000, duty_cycle=0) # Verde
blue_pin = pwmio.PWMOut(board.A6, frequency=5000, duty_cycle=0)  # Azul

# Definir colores (en formato de tupla RGB con valores PWM de 16 bits)
colors = [
    (65535, 0, 0),    # Rojo
    (0, 65535, 0),    # Verde
    (0, 0, 65535),    # Azul
    (65535, 65535, 0),# Amarillo
    (0, 65535, 65535),# Cyan
    (65535, 0, 65535),# Magenta
    (0, 0, 0),        # Apagar
]

# Inicializar los botones
button_a = digitalio.DigitalInOut(board.BUTTON_A)
button_a.switch_to_input(pull=digitalio.Pull.DOWN)

button_b = digitalio.DigitalInOut(board.BUTTON_B)
button_b.switch_to_input(pull=digitalio.Pull.DOWN)

# Función para ajustar el color
def set_color(red, green, blue, brightness):
    # Ajustar cada canal según el brillo aplicando duty_cycle
    red_pin.duty_cycle = int(red * brightness)
    green_pin.duty_cycle = int(green * brightness)
    blue_pin.duty_cycle = int(blue * brightness)

# Brillo inicial y control de colores
current_color = 0
brightness = 1.0  # Brillo inicial al 100%

try:
    while True:
        # Cambiar el color si ambos botones están presionados al mismo tiempo
        if button_a.value and button_b.value:
            current_color = (current_color + 1) % len(colors)
            set_color(*colors[current_color], brightness)
            time.sleep(0.3)

        # Disminuir el brillo si solo se presiona el botón A
        elif button_a.value:
            brightness = max(0, brightness - 0.1)  # Reducir brillo hasta 0 (apagado)
            set_color(*colors[current_color], brightness)
            time.sleep(0.3)

        # Aumentar el brillo si solo se presiona el botón B
        elif button_b.value:
            brightness = min(1, brightness + 0.1)  # Aumentar brillo pero no más del 100%
            set_color(*colors[current_color], brightness)
            time.sleep(0.3)

except KeyboardInterrupt:
    # Apagar las luces en caso de interrupción (Ctrl+C)
    set_color(0, 0, 0, 0)
