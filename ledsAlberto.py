#bibliotecas
from machine import Pin
from neopixel import NeoPixel
from time import sleep

# Configuração dos leds
num_pixels = 10
strip_pin = Pin(0, Pin.OUT)
fita = NeoPixel(strip_pin, num_pixels)

while True:
    for i in range(num_pixels):
        fita.fill((125,125,125))
        fita[i] = (125,0,0)
        fita.write()
        sleep(0.06)
    