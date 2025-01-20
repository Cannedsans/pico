import time
import neopixel
from machine import Pin

# Configurações
NUM_PIXELS = 10  # Número de LEDs na tira
PIN = 0          # Pino GPIO usado para controlar os LEDs

# Inicializando a tira LED
pixels = neopixel.NeoPixel(Pin(PIN), NUM_PIXELS)

# Função para gerar cores em um espectro arco-íris
def wheel(pos):
    """Gera cores ao longo de um espectro RGB."""
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (pos * 3, 255 - pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (255 - pos * 3, 0, pos * 3)
    pos -= 170
    return (0, pos * 3, 255 - pos * 3)

# Função arco-íris
def rainbow(delay):
    """Mostra o efeito de arco-íris na tira LED."""
    for j in range(255):
        for i in range(NUM_PIXELS):
            pixel_index = (i * 256 // NUM_PIXELS) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.write()
        time.sleep(delay)

# Loop infinito para o efeito arco-íris
while True:
    rainbow(0.02)  # Ajuste o atraso para controlar a velocidade
