import time
import math
import array
import audiobusio
import board
import neopixel

# Configuración de NeoPixel
PIN = board.A1
NUMPIXELS = 64
WIDTH = 8
HEIGHT = 8
BRIGHTNESS = 0.2

# Inicializa NeoPixel
pixels = neopixel.NeoPixel(PIN, NUMPIXELS, brightness=BRIGHTNESS, auto_write=False)
hueOffset = 0  # Desplazamiento del gradiente de color

# Inicializa el micrófono con un tamaño de muestra más pequeño para mayor reactividad
mic = audiobusio.PDMIn(board.MICROPHONE_CLOCK, board.MICROPHONE_DATA,
                       sample_rate=16000, bit_depth=16)
NUM_SAMPLES = 80  # Reducido para mayor frecuencia de actualización
samples = array.array('H', [0] * NUM_SAMPLES)

# Función para calcular RMS (Root Mean Square) del audio
def normalized_rms(values):
    minbuf = int(mean(values))
    samples_sum = sum(
        float(sample - minbuf) * (sample - minbuf)
        for sample in values
    )
    return math.sqrt(samples_sum / len(values))

def mean(values):
    return sum(values) / len(values)

# Función de conversión HSV a RGB
def HSVtoRGB(h, s, v):
    h = h / 255.0
    s = s / 255.0
    v = v / 255.0
    i = int(h * 6)
    f = (h * 6) - i
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    i %= 6
    if i == 0:
        r, g, b = v, t, p
    elif i == 1:
        r, g, b = q, v, p
    elif i == 2:
        r, g, b = p, v, t
    elif i == 3:
        r, g, b = p, q, v
    elif i == 4:
        r, g, b = t, p, v
    elif i == 5:
        r, g, b = v, p, q
    return int(r * 255), int(g * 255), int(b * 255)

# Bucle principal
while True:
    mic.record(samples, len(samples))
    volume = normalized_rms(samples)
    
    # Escalar el volumen para afectar la velocidad
    # Cuanto mayor sea el volumen, mayor será la velocidad
    speed = 0.05 + min(volume / 1000, 0.5)  # Ajusta el divisor para modificar la sensibilidad
    hueOffset += speed  # Ajusta la velocidad de desplazamiento

    for y in range(HEIGHT):
        for x in range(WIDTH):
            index = x + y * WIDTH
            hue = 128 + 54 * math.sin(x * 0.4 + math.sin(y * 0.2 + hueOffset))
            r, g, b = HSVtoRGB(hue, 255, int(255 * (volume / 300)))  # Ajusta el brillo según el volumen
            pixels[index] = (r, g, b)
    
    pixels.show()
    time.sleep(0.01)  # Intervalo de actualización rápido para mayor reactividad
