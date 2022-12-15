#------------------------------
#Ejercicio: 2_3 práctica p3 sensores y actuadores
#Autores: Jorge Martín y Rebeca Sánchez
#Fecha límite de entrega: 16/11/22
#Objetivo: encender dos leds con el método add_event_detect
#------------------------------

import time
import signal
import sys
import RPi.GPIO as GPIO


PRESENCIA = 10
LED_VERDE = 32
BOUNCETIME = 500
PRESION = 12
TIME = 1


def callbackSalir (senial, cuadro): # señal y estado cuando se produjo la interrup.
    GPIO.cleanup () # limpieza de los recursos GPIO antes de salir
    sys.exit(0)

def callbackPresencia (canal):
    print("Detectando personas...")
    GPIO.output(LED_VERDE, GPIO.LOW)
    segundos = 0 #comenzamos por 0 para que sean 30 segundos exactos
    while segundos < 30:
        if (GPIO.input(PRESENCIA)==0):
            segundos = segundos + TIME
            time.sleep(TIME)
        if (GPIO.input(PRESENCIA)==1):
            print ("Movimiento detectado")
            GPIO.output(LED_VERDE, GPIO.HIGH)
            time.sleep(5)
            GPIO.output(LED_VERDE, GPIO.LOW)
            segundos = 31
             

if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD)
    #Establecer leds y pulsadores
    GPIO.setup(PRESENCIA, GPIO.IN)
    GPIO.setup(PRESION, GPIO.IN,pull_up_down=GPIO.PUD_UP)
   
    GPIO.setwarnings(False)
    GPIO.setup(LED_VERDE, GPIO.OUT)
    
        
    while True:
        #crear eventos y callback
        GPIO.add_event_detect(PRESION, GPIO.FALLING,callback=callbackPresencia, bouncetime = BOUNCETIME)

        signal.signal(signal.SIGINT, callbackSalir) # callback para CTRL+C
        signal.pause() # esperamos por hilo/callback CTRL+C antes de acabar
        
        time.sleep(1)
                
if __name__=="__main__":
     main()
     
