#include <Adafruit_CircuitPlayground.h>

const int trigPin = A1;
const int echoPin = A2;

void setup() {
  Serial.begin(9600);
  CircuitPlayground.begin();
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  // Generar pulso de activación para el HC-SR04
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Leer el tiempo de duración del pulso de eco
  long duration = pulseIn(echoPin, HIGH);
  
  // Convertir duración en distancia
  float distance = (duration * 0.0343) / 2;
  
  // Mostrar la distancia en el monitor serial
  Serial.print("Distancia: ");
  Serial.print(distance);
  Serial.println(" cm");

  // Cambiar el color de todos los NeoPixels según la distancia
  if (distance < 10) {
    for (int i = 0; i < 10; i++) {
      CircuitPlayground.setPixelColor(i, 255, 0, 0); // Rojo
    }
  } else if (distance < 30) {
    for (int i = 0; i < 10; i++) {
      CircuitPlayground.setPixelColor(i, 255, 128, 0); // Naranja
    }
  } else if (distance < 50) {
    for (int i = 0; i < 10; i++) {
      CircuitPlayground.setPixelColor(i, 255, 255, 0); // Amarillo
    }
  } else if (distance < 70) {
    for (int i = 0; i < 10; i++) {
      CircuitPlayground.setPixelColor(i, 0, 255, 0); // Verde
    }
  } else if (distance < 100) {
    for (int i = 0; i < 10; i++) {
      CircuitPlayground.setPixelColor(i, 0, 0, 255); // Azul
    }
  } else {
    CircuitPlayground.clearPixels(); // Apagar si está fuera del rango de 100 cm
  }
  
  delay(100); // Pequeña pausa para estabilidad
}
