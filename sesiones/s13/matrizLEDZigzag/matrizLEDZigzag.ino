#include <Adafruit_NeoPixel.h>

#define PIN        A3     // Pin de datos de la matriz NeoPixel
#define NUMPIXELS  64     // Número de LEDs en la matriz
#define WIDTH      8      // Ancho de la matriz
#define HEIGHT     8      // Alto de la matriz

Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

float hueOffset = 0;      // Desplazamiento para animar el gradiente
bool zigzag = false;       // Activar o desactivar el modo zigzag

void setup() {
  strip.begin();
  strip.setBrightness(51); 
  strip.show();            // Apaga todos los LEDs al inicio
}

void loop() {
  hueOffset += 0.03;       // Velocidad del desplazamiento del gradiente
  for (int y = 0; y < HEIGHT; y++) {
    for (int x = 0; x < WIDTH; x++) {
      int index;
      if (zigzag && y % 2 == 1) {
        // Modo zigzag: invertir el índice de las filas pares
        index = (y + 1) * WIDTH - x - 1;
      } else {
        // Modo normal
        index = x + y * WIDTH;
      }

      // Generar un valor de tono (hue) que varía en una onda sinusoidal deformada
      float hue = 128 + 127 * sin(x * 0.4 + sin(y * 0.2 + hueOffset)); // Escala a 0-255
      
      // Convertir HSV a RGB y configurar el color del LED
      uint32_t color = HSVtoRGB((int)hue, 255, 255);
      strip.setPixelColor(index, color);
    }
  }
  strip.show();
  delay(30);               // Intervalo de actualización para suavidad
}

// Función para convertir HSV a RGB
uint32_t HSVtoRGB(int h, int s, int v) {
  float hh, p, q, t, ff;
  long i;
  float r, g, b;

  if(s <= 0.0) {
    r = v;
    g = v;
    b = v;
    return strip.Color(r, g, b);
  }
  
  hh = h;
  if(hh >= 360.0) hh = 0.0;
  hh /= 60.0;
  i = (long)hh;
  ff = hh - i;
  p = v * (1.0 - (s / 255.0));
  q = v * (1.0 - (s / 255.0) * ff);
  t = v * (1.0 - (s / 255.0) * (1.0 - ff));

  switch(i) {
    case 0:
      r = v;
      g = t;
      b = p;
      break;
    case 1:
      r = q;
      g = v;
      b = p;
      break;
    case 2:
      r = p;
      g = v;
      b = t;
      break;
    case 3:
      r = p;
      g = q;
      b = v;
      break;
    case 4:
      r = t;
      g = p;
      b = v;
      break;
    case 5:
    default:
      r = v;
      g = p;
      b = q;
      break;
  }
  return strip.Color((int)r, (int)g, (int)b);
}
