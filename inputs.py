from machine import Pin
from time import sleep

led = Pin(25, Pin.OUT)
bnt = Pin(16, Pin.IN, Pin.PULL_UP)

while True:
    if bnt.value() == 0: 
        led.value(1)
    else:
        led.value(0)