import time
from adafruit_circuitplayground import cp # Instancia de una clase cp que específicamente hace referencia ala CPX 

# Nota: Diferencia entre variable y objeto. 

# Variables: Son etiquetas o nombres que referencian a objetos.
# Objetos: Son instancias de tipos de datos que contienen el valor y tienen comportamientos definidos por su tipo.

# Lista de colores en formato RGB
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Rojo, Verde, Azul
current_color = 0  # Índice del color actual

def update_color():
    cp.pixels.fill(colors[current_color])

update_color()  # Inicializa con el primer color

while True:
    if cp.button_a:  # Si se presiona el botón A
        current_color = (current_color - 1) % len(colors)  # Cambia al color anterior
        # La función len obtiene la cantidad de elementos que tiene un objeto.
        # En otros lenguajes de programación es length supongo que de ahí el nombre. 
        update_color()
        time.sleep(0.2)  # Pequeña pausa para evitar cambios múltiples con un solo toque

    if cp.button_b:  # Si se presiona el botón B
        current_color = (current_color + 1) % len(colors)  # Cambia al siguiente color
        update_color()
        time.sleep(0.2)  # Pequeña pausa para evitar cambios múltiples con un solo toque
