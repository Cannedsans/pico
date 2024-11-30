from machine import Pin
from neopixel import NeoPixel
from time import sleep
import _thread

strip_pin = Pin(0, Pin.OUT)
pixels = 10
strip = NeoPixel(strip_pin, pixels)

def led():
    while(True):
        for i in range(pixels):
            strip[i] = (255,0,0)
            strip.write()
            sleep(0.5)
        for i in range(pixels):
            strip[i] = (0,0,255)
            strip.write()
            sleep(0.5)

_thread.start_new_thread(led, ())

led = Pin(25, Pin.OUT)
while(True):
    led.toggle()
    sleep(1)
