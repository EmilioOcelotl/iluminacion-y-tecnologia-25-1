#include <Adafruit_NeoPixel.h>

#include <Adafruit_CircuitPlayground.h>

// Configuración del sensor ultrasónico
const int trigPin = A1;
const int echoPin = A2;
float alpha = 0.1; // Factor de suavizado (0.0 - 1.0), cuanto más bajo, más suave
long smoothedDistance = 0;

// Configuración de la tira de LEDs
const int ledPin = A3; // Pin donde se conecta la tira de LEDs
const int numLeds = 64; // Número total de LEDs en la tira
Adafruit_NeoPixel strip = Adafruit_NeoPixel(numLeds, ledPin, NEO_GRB + NEO_KHZ800);

// Configuración de la matriz
const int width = 8; // Ancho de la matriz
const int height = 8; // Alto de la matriz

// Variables para el modo
int mode = 2; // 1 para la primera opción, 2 para la segunda opción
long distance = 0;

/*
 long readUltrasonicDistance() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  long duration = pulseIn(echoPin, HIGH);
  return duration * 0.034 / 2;
} 
 */
long readUltrasonicDistance() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  long duration = pulseIn(echoPin, HIGH);
  long distance = duration * 0.034 / 2;

  // Aplicar el filtro exponencial
  smoothedDistance = (alpha * distance) + ((1 - alpha) * smoothedDistance);
  return smoothedDistance;
}
// Función para encender los LEDs en filas alternas (Modo 1)
void alternateRows() {
  distance = readUltrasonicDistance();
  int offset = map(distance, 5, 50, 0, height); // Ajusta el valor de acuerdo a la distancia
  
  strip.clear();
  for (int row = 0; row < height; row++) {
    for (int col = 0; col < width; col++) {
      int index = row % 3 == 0 ? col + row * width : (width - 1 - col) + row * width;
      if ((row + offset) % 3 == 0) {
        strip.setPixelColor(index, strip.Color(255, 255, 255)); // Color azul
      }
    }
  }
  strip.show();
}

void movingColors() {
  distance = readUltrasonicDistance();
  int offset = map(distance, 5, 50, 0, 20); // Ajusta el desplazamiento basado en la distancia

  strip.clear();
  
  for (int i = 0; i < numLeds; i++) {
    // Calcular la posición desplazada del LED considerando el offset
    int pos = (i + offset) % numLeds;

    // Determinar si el LED está en una franja encendida o apagada
    if ((i / 10) % 2 == 0) { // Si estamos en una franja encendida
      // Distribuir los valores de rojo de 0 a 255 en los 10 LEDs encendidos
      //int redValue = map(i % 10, 0, 9, 0, 255);
      strip.setPixelColor(pos, strip.Color(255, 255, 255)); // Color rojo
    }
    // Si estamos en una franja apagada, no se establece ningún color
  }
  
  strip.show();
}



void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  
  strip.begin();
  strip.show();
  
  if (mode == 1) {
    alternateRows();
  } else if (mode == 2) {
    movingColors();
  }
}

void loop() {
  if (mode == 1) {
    alternateRows();
  } else if (mode == 2) {
    movingColors();
  }
  delay(50); // Ajusta el retraso según sea necesario
}
