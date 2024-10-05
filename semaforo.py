from machine import Pin
from time import sleep

red = Pin(20,Pin.OUT)
yellow = Pin(19,Pin.OUT)
green = Pin(18,Pin.OUT)

while True:
    red.value(1)
    green.value(0)
    yellow.value(0)
    sleep(1)
    red.value(0)
    yellow.value(1)
    sleep(1)
    yellow.value(0)
    green.value(1)
    sleep(1)