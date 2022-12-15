# P8-Fuerza
## Introducción
EL objetivo de esta práctica es eprender el funcionamiento de los sensores de presión y presencia. Eneste caso, el ejercicio final será la unión de estos dos para un objetivo práctico y real que podría suceder.

## Componentes
El sensor de presión que vamos a utlizar será un sensor de fuerza piezorresistivo modelo [FSR](https://www.electronicoscaldas.com/datasheet/FSR-Integration_Guide_Interlink.pdf). Nosotros lo vamos a emplear en modo digital (Low/High), para ello vamos a utilizar una resistencia de 1MΩ que sirve para cerrar el circuito y leer el estado. Para conectarlo a la placa lo único que haremos será conectar una pata directamente a 5V y la otra, junto con la resistencia, a un puerto GPIO.

El sensor de presencia [HC-SR501](https://www.mpja.com/download/31227sc.pdf). Este sensor, de alguna maner, es un detector de luz, pero de luz infrarroja muy débil que emitimos los seres humanos (y que no podemos detectar). Para conectarlo a la placa, un pin va directo a 5V, otro a GND y el tercero a un pin GPIO, el cual lo leerá de forma digital (Low/High). Además, tiene dos ruedecitas con las que podremos calibrarlo para que sea más **sensitivo** a la lluz infrarroja o el tiempo en el que permanece en HIGH. Además, posee un jumper. 

Finalmente, los componenetes utilizados son:
- Sensor de presencia
- Sensor de presión
- Resistencia 1MΩ
- Led verde
- Resistencia 220Ω

## Circuito
El esquema del circuito final quedaría de la siguiente manera:

AÑADIR FOTO


## Ejercicios
Para el primer ejercicio nos pedía implementar un código lo más sencillo y eficiente posible para el sensor de presencia. Para ello, hemos recliclado el código de la práctica anterior cambiando los nombres y quitando alguna que otra cosa. De esta forma, el código se queda sencillo y no se peta mucho la placa pues el time.sleep() es considerable para que el input no se sature:

Para el segundo código, hemos hecho lo mismo, reclicar código y cambiar nombres. El código más genérico sería pues:
```python
import RPi.GPIO as GPIO
import time

SENSOR = x
TIME = y
GPIO.setmode(GPIO.BOARD)
GPIO.setup(SENSOR, GPIO.IN)

while True:
    if (GPIO.input(SENSOR)==0):
        print ("LOW")
    if (GPIO.input(SENSOR)==1):
        print ("HIGH")
    time.sleep(TIME)
```

Finalmente, para el último ejercicio, para no tener que utilizar dos input, hemos decicido añadir un evento al sensor de presión, y una vez este lo haya detectado que leea el input del sensor de movimiento. De esta forma no saturamos tanto la placa y si no se ha leido nada se queda en stand by. Para entender el funcionamiento, hemos puesto a continuación lo mostrado en la terminal junto con lo sudecido en el sensor:

Sensor de presencia:

![Sensor de presencia](https://github.com/rsanchez2021/Image/blob/main/sensor_movimiento.gif)
```bash
ñaih
ahv
```

Sensor de presióm:

![Sensor de presiñon](https://github.com/rsanchez2021/Image/blob/main/sensor_presion.gif)

```bash
paoj
poj
```


    
