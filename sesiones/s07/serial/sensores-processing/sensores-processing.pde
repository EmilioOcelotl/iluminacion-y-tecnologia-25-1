import processing.serial.*;

Serial myPort;  // El puerto serial

void setup() {
  String[] puertos = Serial.list();
  myPort = new Serial(this, puertos[0], 115200);  // Cambia el índice si es necesario
}

void draw() {
  if (myPort.available() > 0) {
    String inData = myPort.readStringUntil('\n');  // Leer hasta nueva línea
    if (inData != null) {
      inData = inData.trim();  // Limpiar espacios
      String[] valores = inData.split(",");  // Separar los valores

      // Comprobar que se recibieron los valores esperados
      if (valores.length == 5) {
        // Imprimir los valores en la consola
        println("Luz: " + valores[0]);
        // println("Sonido: " + valores[1]);
        println("Temperatura: " + valores[1]);
        println("Acelerómetro: (" + valores[2] + ", " + valores[3] + ", " + valores[4] + ")");
      } else {
        println("Error: número inesperado de valores recibidos");
      }
    }
  }
}
