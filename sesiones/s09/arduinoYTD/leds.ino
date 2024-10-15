#include <Adafruit_CircuitPlayground.h>

void setup() {
  Serial.begin(9600);          // Inicializa la comunicación serial a 9600 bps
  CircuitPlayground.begin();   // Inicializa la placa Circuit Playground
  pinMode(13, OUTPUT);         // Configura el LED 13 como salida
}

void loop() {
  if (Serial.available()) {    // Verifica si hay datos disponibles
    char data = Serial.read(); // Lee un byte de la serie
    Serial.print("Dato recibido: "); // Muestra el dato para depuración
    Serial.println(data);

    if (data == '1') {
      digitalWrite(13, HIGH);   // Enciende el LED 13
      // Enciende todos los NeoPixels en rojo
      for (int i = 0; i < 10; i++) { // Hay 10 NeoPixels en total
        CircuitPlayground.setPixelColor(i, 255, 0, 0); // Rojo
      }
      Serial.println("LEDs encendidos");
    } 
    else if (data == '0') {
      digitalWrite(13, LOW);    // Apaga el LED 13
      CircuitPlayground.clearPixels(); // Apaga todos los NeoPixels
      Serial.println("LEDs apagados");
    }
    else {
      Serial.println("Dato no válido");
    }
  }
}
