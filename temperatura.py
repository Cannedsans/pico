from machine import ADC #serve para usar valores analógicos
from time import sleep

sensor=ADC(4)#sensor de temperatura interno da pico 

while(True):
    leitura =(sensor.read_u16()*3.3)/65535 #calculo da saida do sensor com resolução de 16bits
    temperatura = 27 -(leitura  - 0.706)/0.001721 #calculo da teperatura segundo o fabricante
    print("Temperatura:",temperatura)
    sleep(1)