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

  // Normalizar la distancia para obtener un valor entre 0 y 255
  int colorValue = map(distance, 0, 100, 0, 255);

  // Calcular los valores de color para el gradiente de rojo a violeta
  int red = max(255 - colorValue, 0);       // Disminuye de 255 a 0
  int blue = min(colorValue, 255);          // Aumenta de 0 a 255
  int green = 0;                            // Verde permanece en 0 para un efecto de gradiente limpio

  // Aplicar el color calculado a todos los NeoPixels
  for (int i = 0; i < 10; i++) {
    CircuitPlayground.setPixelColor(i, red, green, blue);
  }

  delay(100); // Pequeña pausa para estabilidad
}
