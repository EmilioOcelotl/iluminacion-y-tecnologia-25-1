// Para activar el código es necesario entrar a la siguiente liga y generar imagenes como datos: 

// https://editor.p5js.org/emilioocelotl/sketches/LL_nuDLKr

// Es importante hacer una copia para poder agregar imágenes al proyecto y poder generar nuevas imágenes

// También es importante determinar el tamaño de la matriz para que se puedan generar los archivos

#include <Adafruit_NeoPixel.h>
#include <Adafruit_CircuitPlayground.h>

// Configuración de NeoPixel
#define NUM_PIXELS 64    // Número total de LEDs en la tira
#define DATA_PIN A1       // Pin de datos
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUM_PIXELS, DATA_PIN, NEO_GRB + NEO_KHZ800);

// Tamaño de la matriz LED (15x15)
const int matrixWidth = 8;
const int matrixHeight = 8;

// Imágenes almacenadas como arreglos RGB. Por favor sustituyan image por image + el número de la imagen 

const uint8_t image1[matrixHeight][matrixWidth][3] = {
    // Datos generados por p5.js para la imagen 1
};

const uint8_t image2[matrixHeight][matrixWidth][3] = {
    // Datos generados por p5.js para la imagen 2
};

const uint8_t image3[matrixHeight][matrixWidth][3] = {
    // Datos generados por p5.js para la imagen 3
};

// Arreglo de imágenes
const uint8_t (*images[3])[matrixWidth][3] = {image1, image2, image3};

// Configuración del micrófono
#define CLAP_THRESHOLD 90  // Umbral para detectar un aplauso

// Estado inicial
int currentImage = 0;      // Imagen actual
bool transitioning = false; // Si está en transición

void setup() {
  // Inicializar Circuit Playground y NeoPixel
  CircuitPlayground.begin();
  strip.begin();
  strip.show(); // Apagar LEDs

  // Mostrar primera imagen
  showImage(images[currentImage]);
}

void loop() {
  // Leer el valor del micrófono
  int micValue = CircuitPlayground.mic.soundPressureLevel(50); // 50 ms de muestra

  // Detectar si el valor supera el umbral (aplauso)
  if (micValue > CLAP_THRESHOLD && !transitioning) {
    transitioning = true; // Evitar múltiples cambios rápidos
    nextImage();          // Cambiar a la siguiente imagen
    delay(300);           // Tiempo de espera para evitar detecciones duplicadas
  }
}

// Mostrar una imagen en la tira NeoPixel
void showImage(const uint8_t image[matrixHeight][matrixWidth][3]) {
  int ledIndex = 0; // Índice de LED en la tira
  for (int y = 0; y < matrixHeight; y++) {
    for (int x = 0; x < matrixWidth; x++) {
      uint8_t r = image[y][x][0];
      uint8_t g = image[y][x][1];
      uint8_t b = image[y][x][2];
      strip.setPixelColor(ledIndex, strip.Color(r, g, b));
      ledIndex++;
    }
  }
  strip.show(); // Actualizar la tira
}

// Cambiar a la siguiente imagen con una transición suave
void nextImage() {
  int nextImageIndex = (currentImage + 1) % 3; // Siguiente imagen (circular)
  const uint8_t (*currentImg)[matrixWidth][3] = images[currentImage];
  const uint8_t (*nextImg)[matrixWidth][3] = images[nextImageIndex];

  // Transición suave
  for (int step = 0; step <= 100; step++) {
    int ledIndex = 0;
    for (int y = 0; y < matrixHeight; y++) {
      for (int x = 0; x < matrixWidth; x++) {
        // Mezclar colores de la imagen actual y la siguiente
        uint8_t r = map(step, 0, 100, currentImg[y][x][0], nextImg[y][x][0]);
        uint8_t g = map(step, 0, 100, currentImg[y][x][1], nextImg[y][x][1]);
        uint8_t b = map(step, 0, 100, currentImg[y][x][2], nextImg[y][x][2]);
        strip.setPixelColor(ledIndex, strip.Color(r, g, b));
        ledIndex++;
      }
    }
    strip.show();
    delay(5); // Controlar la velocidad de la transición
  }

  // Actualizar estado
  currentImage = nextImageIndex;
  transitioning = false; // Permitir futuros cambios
}
