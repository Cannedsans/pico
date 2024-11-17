from machine import Pin   
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
from time import sleep

config_i2c=I2C(0,sda=Pin(0),scl=Pin(1),freq=40000)
tela = I2cLcd(config_i2c, 0x27, 2,16)

while(True):
    tela.clear()
    tela.move_to(0,0)
    tela.putstr("Ola mundo")
    sleep(1)
    tela.clear()
    tela.move_to(0,0)
    tela.putstr("na rasp pico!")
    sleep(1)
