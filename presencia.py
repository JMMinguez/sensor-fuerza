#------------------------------
#Ejercicio: Práctica p8 sensores y actuadores --> Sensor fuerza y presencia
#Autores: Jorge Martín y Rebeca Sánchez
#Fecha límite de entrega: 15/12/22
#Objetivo: detectar movimiento con el sensor de presencia
#------------------------------
#!/usr/bin/python
import RPi.GPIO as GPIO
import time


#establecer pines
PRESENCIA = 10
TIME = 0.5
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PRESENCIA, GPIO.IN)

while True:
    if (GPIO.input(PRESENCIA)==0):
        print ("No hay ningún movimiento")
    if (GPIO.input(PRESENCIA)==1):
        print ("Movimiento detectado")
    time.sleep(TIME)

#-------------------------------
#CASOS DE USO
#-Hay veces que el sensor tarda un poco en detectar por el sllep
# se soluciona disminuyendolo. 
