import time
import board
from adafruit_circuitplayground import cp

while True:
    # Leer valores de los sensores
    luz = cp.light  # Sensor de luz
    # sonido = cp.sound  # Sensor de sonido
    temperatura = cp.temperature  # Sensor de temperatura
    acelerometro = cp.acceleration  # Acelerómetro

    # Enviar los datos como una cadena de texto
    datos = f"{luz},{temperatura},{acelerometro[0]},{acelerometro[1]},{acelerometro[2]}"
    print(datos)  # Asegúrate de que se envíen los datos
    time.sleep(0.5)  # Ajusta el tiempo según sea necesario
