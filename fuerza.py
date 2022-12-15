#------------------------------
#Ejercicio: Práctica p8 sensores y actuadores --> Sensor fuerza y presencia
#Autores: Jorge Martín y Rebeca Sánchez
#Fecha límite de entrega: 15/12/22
#Objetivo: detectar presión con el sensor de presión
#------------------------------
#!/usr/bin/python
import RPi.GPIO as GPIO
import time


#establecer pines
PRESENCIA = 12
TIME = 0.5
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PRESENCIA, GPIO.IN)

while True:
    if (GPIO.input(PRESENCIA)==0):
        print ("No hay presión")
    if (GPIO.input(PRESENCIA)==1):
        print ("Presión detectada")
    time.sleep(TIME)
