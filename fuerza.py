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
PRESION = 12
TIME = 0.5
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PRESION, GPIO.IN)

while True:
    if (GPIO.input(PRESION)==0):
        print ("No hay presión")
    if (GPIO.input(PRESION)==1):
        print ("Presión detectada")
    time.sleep(TIME)
