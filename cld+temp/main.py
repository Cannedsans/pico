from machine import Pin,ADC,I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
from time import sleep

config_i2c=I2C(0,sda=Pin(0),scl=Pin(1),freq=40000)
tela = I2cLcd(config_i2c, 0x27, 2,16)
sensor=ADC(4)
old = 0
while(True):
    leitura =(sensor.read_u16()*3.3)/65535 #calculo da saida do sensor com resolução de 16bits
    temperatura = 27 -(leitura  - 0.706)/0.001721 #calculo da teperatura segundo o fabricante
    if(leitura !=old):
        tela.clear()
        tela.move_to(0,0)
        tela.putstr("Temperatura.:")
        tela.move_to(0,1)
        tela.putstr(str(round(temperatura, 1)))
        old = round(temperatura,1)
    sleep(1)