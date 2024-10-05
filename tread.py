from machine import Pin
from time import sleep
import _thread

#============= Configuração =================#
red = Pin(20, Pin.OUT)
yellow = Pin(19, Pin.OUT)
green = Pin(18, Pin.OUT)
bnt = Pin(16, Pin.IN, Pin.PULL_UP)  # Configuração do botão com pull-up
interno = Pin(25, Pin.OUT)  # LED interno da Pico

#============ thread =================#
def apertado():
    while True:
        if bnt.value() == 0:  # Corrigido para usar bnt.value()
            interno.toggle()  # Alterna o estado do LED interno
        sleep(0.1)  # Espera para evitar leituras muito rápidas (debounce)

# Iniciar a thread
_thread.start_new_thread(apertado, ())

#============ main =================#
while True:
    red.value(1)      # Liga o LED vermelho
    green.value(0)    # Desliga o LED verde
    yellow.value(0)   # Desliga o LED amarelo
    sleep(1)          # Espera 1 segundo

    red.value(0)      # Desliga o LED vermelho
    yellow.value(1)   # Liga o LED amarelo
    sleep(1)          # Espera 1 segundo

    yellow.value(0)   # Desliga o LED amarelo
    green.value(1)    # Liga o LED verde
    sleep(1)          # Espera 1 segundo
