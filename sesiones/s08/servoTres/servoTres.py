import time
import board
import pwmio
from adafruit_motor import servo
from adafruit_circuitplayground import cp

pwm = pwmio.PWMOut(board.A1, duty_cycle=0, frequency=50)

mi_servo = servo.Servo(pwm)

angulo_actual = 0  
incremento = 20  

while True:
    if cp.button_a:
        angulo_actual += incremento
        if angulo_actual > 180:
            angulo_actual = 0  
        mi_servo.angle = angulo_actual
        print("Avanzando en un sentido:", angulo_actual)
        time.sleep(0.1)  

    elif cp.button_b:
        angulo_actual -= incremento
        if angulo_actual < 0:
            angulo_actual = 180  
        mi_servo.angle = angulo_actual
        print("Avanzando en el sentido contrario:", angulo_actual)
        time.sleep(0.1)  

    time.sleep(0.05) 