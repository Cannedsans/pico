from machine import Pin
from time import sleep

pir = Pin(16,Pin.IN, Pin.PULL_DOWN)
led = Pin(25,Pin.OUT)

while True:
    if (pir.value()):
        led.toggle()
        sleep(0.1)
