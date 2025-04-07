#include <Adafruit_NeoPixel.h>

#define PIN 4         // Pin donde conectas el NeoPixel (ajusta si es necesario)
#define NUMPIXELS 3    // Número de LEDs en la tira (en este caso, solo 1)

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

    int firstComma = data.indexOf(',');
    int secondComma = data.indexOf(',', firstComma + 1);
    int thirdComma = data.indexOf(',', secondComma + 1);

    // Validar el formato del mensaje antes de proceder
    if (firstComma > 0 && secondComma > firstComma && thirdComma > secondComma) {
      int state = data.substring(0, firstComma).toInt();
      int red = data.substring(firstComma + 1, secondComma).toInt();
      int green = data.substring(secondComma + 1, thirdComma).toInt();
      int blue = data.substring(thirdComma + 1).toInt();

      if (state == 1) {
        digitalWrite(13, HIGH);
        for (int i = 0; i < NUMPIXELS; i++) {
          strip.setPixelColor(i, strip.Color(red, green, blue));
        }
        strip.show();
        Serial.println("LED y NeoPixel encendidos");
      } else if (state == 0) {
        digitalWrite(13, LOW);
        for (int i = 0; i < NUMPIXELS; i++) {
          strip.setPixelColor(i, strip.Color(0, 0, 0)); // Apagar cada LED sin usar clear
        }
        strip.show();
        Serial.println("LED y NeoPixel apagados");
      } else {
        Serial.println("Dato no válido");
      }
    } else {
      Serial.println("Formato de dato incorrecto");
    }
  }
}
