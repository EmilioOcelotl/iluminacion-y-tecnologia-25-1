# SPDX-FileCopyrightText: 2017 John Edgar Park for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# Circuit Playground Temperature and NeoPixel Visualization
# Reads the on-board temperature sensor and visualizes the temperature with NeoPixels

# Pruebas con un congelador

import time
import board
import neopixel
import adafruit_thermistor
import simpleio

# Initialize NeoPixels
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.05, auto_write=False)
pixels.fill((0, 0, 0))
pixels.show()

# Initialize Thermistor
thermistor = adafruit_thermistor.Thermistor(
    board.TEMPERATURE, 10000, 10000, 25, 3950)

while True:
    # Read temperature
    temp_c = thermistor.temperature

    # Map temperature to pixel position
    # Assuming a temperature range of 0°C to 40°C (you can adjust this as needed)
    pixel_count = 10
    min_temp = 0
    max_temp = 40
    peak = simpleio.map_range(temp_c, min_temp, max_temp, 0, pixel_count - 1)
    
    # Print the temperature for debugging
    temp_f = temp_c * 9 / 5 + 32
    print("Temperature is: %f C and %f F" % (temp_c, temp_f))
    print(int(peak))
    
    # Update NeoPixels based on temperature
    for i in range(pixel_count):
        if i <= peak:
            pixels[i] = (0, 255, 0)  # Green for active pixels
        else:
            pixels[i] = (0, 0, 0)    # Off for inactive pixels
    pixels.show()

    time.sleep(0.25)
