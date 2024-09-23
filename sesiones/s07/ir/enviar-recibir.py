import time
import board
import pulseio
import adafruit_irremote
from adafruit_circuitplayground import cp

# Configuración del transmisor y codificador infrarrojo
ir_transmitter = pulseio.PWMOut(board.IR_TX, frequency=38000, duty_cycle=2 ** 15)
ir_encoder = adafruit_irremote.GenericTransmit(header=[9500, 4500], one=[550, 550], zero=[550, 1500])

# Configuración del receptor y decodificador infrarrojo
ir_receiver = pulseio.PulseIn(board.IR_RX, maxlen=120, idle_state=True)
ir_decoder = adafruit_irremote.GenericDecode()

# Mensaje a enviar
mensaje_a_enviar = "hola mundo"

def string_a_bytes(mensaje):
    """Convierte un string a una lista de bytes."""
    return list(mensaje.encode("utf-8"))

def bytes_a_string(bytes_recibidos):
    """Convierte una lista de bytes a un string."""
    return bytes(bytes_recibidos).decode("utf-8")

def enviar_mensaje(mensaje):
    """Envía un mensaje infrarrojo codificado como bytes."""
    mensaje_bytes = string_a_bytes(mensaje)
    ir_encoder.transmit(ir_transmitter, mensaje_bytes)
    print(f"Enviando mensaje: {mensaje}")

def recibir_mensaje():
    """Intenta recibir un mensaje infrarrojo y lo decodifica como string."""
    if len(ir_receiver) > 0:
        try:
            pulses = ir_decoder.read_pulses(ir_receiver)
            mensaje_recibido_bytes = ir_decoder.decode_bits(pulses)
            mensaje_recibido = bytes_a_string(mensaje_recibido_bytes)
            print(f"Mensaje recibido: {mensaje_recibido}")
        except adafruit_irremote.IRNECRepeatException:
            pass  
        except adafruit_irremote.IRDecodeException:
            print("No se pudo decodificar el mensaje")
        ir_receiver.clear()

# Bucle principal
while True:
    # Solo enviar mensaje cuando se presione el botón A
    if cp.button_a:
        enviar_mensaje(mensaje_a_enviar)

    recibir_mensaje()

    time.sleep(0.1)