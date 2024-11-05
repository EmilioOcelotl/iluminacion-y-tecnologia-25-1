#include <Adafruit_NeoPixel.h>

#define PIN A1         // Pin donde conectas el NeoPixel (ajusta si es necesario)
#define NUMPIXELS 64   // Número de LEDs en la tira

Adafruit_NeoPixel strip(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  Serial.begin(9600);          // Inicializa la comunicación serial a 9600 bps
  strip.begin();               // Inicializa la tira NeoPixel
  strip.show();                // Apaga todos los LEDs al inicio
  pinMode(13, OUTPUT);         // Configura el LED 13 como salida
  Serial.setTimeout(10);
}

void loop() {
  if (Serial.available()) {
    String data = Serial.readStringUntil('\n');
    data.trim();

    Serial.print("Dato recibido: ");
    Serial.println(data);

    // Convertir el dato recibido en un valor de intensidad
    float intensity = data.toFloat();

    // Validar que el valor esté dentro del rango de 0 a 1
    if (intensity >= 0.0 && intensity <= 1.0) {
      int brightness = (int)(intensity * 255); // Convertir a valor de 0 a 255
      Serial.print("Intensidad: ");
      Serial.println(brightness);

      // Encender los píxeles con el mismo color y el brillo calculado
      for (int i = 0; i < NUMPIXELS; i++) {
        strip.setPixelColor(i, strip.Color(brightness, 0, brightness)); // Blanco
      }
      strip.show();
    } else {
      Serial.println("Valor de intensidad fuera de rango (0-1)");
    }
  }
}
