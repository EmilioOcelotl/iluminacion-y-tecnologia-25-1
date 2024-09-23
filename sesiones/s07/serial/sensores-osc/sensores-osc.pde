import oscP5.*;
import netP5.*;
import processing.serial.*;

Serial myPort;  // El puerto serial
OscP5 oscP5;    // Instancia de OSC
NetAddress destino;  // Dirección de destino para OSC

void setup() {
  String[] puertos = Serial.list();
  myPort = new Serial(this, puertos[0], 115200);  // Cambia el índice si es necesario

  // Configurar OSC
  oscP5 = new OscP5(this, 12000);  // Puerto local para recibir OSC
  destino = new NetAddress("127.0.0.1", 8000);  // Cambia a la dirección y puerto deseados
}

void draw() {
  if (myPort.available() > 0) {
    String inData = myPort.readStringUntil('\n');  // Leer hasta nueva línea
    if (inData != null) {
      inData = inData.trim();  // Limpiar espacios
      String[] valores = inData.split(",");  // Separar los valores

      // Comprobar que se recibieron los valores esperados
      if (valores.length == 5) {
        // Crear y enviar el mensaje OSC
        OscMessage mensaje = new OscMessage("/sensores");
        mensaje.add(float(valores[0]));  // Luz
        mensaje.add(Float.parseFloat(valores[1]));  // Temperatura
        mensaje.add(Float.parseFloat(valores[2]));  // Acelerómetro X
        mensaje.add(Float.parseFloat(valores[3]));  // Acelerómetro Y
        mensaje.add(Float.parseFloat(valores[4]));  // Acelerómetro Z

        oscP5.send(mensaje, destino);  // Enviar el mensaje OSC
        println("Enviando: " + inData);  // Imprimir en la consola
      } else {
        println("Error: número inesperado de valores recibidos");
      }
    }
  }
}
