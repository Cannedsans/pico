from machine import Pin
from neopixel import NeoPixel
from time import sleep

# Configuração do número de LEDs e cor
num_pixels = 10
roxo = (80, 200, 200)  # Cor azul
rosa = (200, 200, 80)
# Configuração do pino de dados da faixa NeoPixel
strip_pin = Pin(0, Pin.OUT)

# Inicialização da faixa NeoPixel
my_strip = NeoPixel(strip_pin, num_pixels)

while True:
    for i in range(num_pixels):
        my_strip.fill(rosa)  # Apaga todos os LEDs
        my_strip[i] = roxo  # Acende o LED atual com a cor definida    
        my_strip.write()  # Atualiza a faixa NeoPixel
        sleep(0.3)  # Atraso de 100ms