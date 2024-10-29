#include <Adafruit_NeoPixel.h>

#define PIN A1         // Pin donde conectas el NeoPixel (ajusta si es necesario)
#define NUMPIXELS 10    // Número de LEDs en la tira (en este caso, solo 1)

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
    String data = Serial.readStringUntil('\n'); // Lee la cadena hasta el salto de línea
    Serial.print("Dato recibido: ");
    Serial.println(data);

    // Divide el mensaje recibido en partes
    int firstComma = data.indexOf(',');
    int secondComma = data.indexOf(',', firstComma + 1);
    int thirdComma = data.indexOf(',', secondComma + 1);

    // Extrae el valor de estado (0 o 1) y colores RGB
    int state = data.substring(0, firstComma).toInt();
    int red = data.substring(firstComma + 1, secondComma).toInt();
    int green = data.substring(secondComma + 1, thirdComma).toInt();
    int blue = data.substring(thirdComma + 1).toInt();

    if (state == 1) {
      digitalWrite(13, HIGH);   // Enciende el LED 13
      for(int i = 0; i < 10;i++){
      strip.setPixelColor(i, strip.Color(red, green, blue)); // Aplica el color recibido al LED 0 de la tira NeoPixel
      }
      strip.show();             // Actualiza la tira para mostrar el color
      Serial.println("LED y NeoPixel encendidos");
    } else if (state == 0) {
      digitalWrite(13, LOW);    // Apaga el LED 13
      strip.clear();            // Apaga el NeoPixel
      strip.show();             // Actualiza la tira para mostrar los cambios
      Serial.println("LED y NeoPixel apagados");
    } else {
      Serial.println("Dato no válido");
    }
  }
}
