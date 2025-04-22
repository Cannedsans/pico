from machine import ADC, Pin
import time

# Define os pinos dos LEDs
led_pins = (9, 10, 11, 12, 13, 14, 15)
leds = [Pin(pin, Pin.OUT) for pin in led_pins]

# Define o potenciômetro no ADC2 (GP28)
pot = ADC(Pin(28))

while True:
    # Lê o valor do potenciômetro (0 a 65535)
    value = pot.read_u16()

    # Converte para número de LEDs a ligar (0 a 7)
    num_leds = int((value / 65534) * len(leds))

    # Liga os LEDs conforme o valor do potenciômetro
    for i, led in enumerate(leds):
        if i <= num_leds:
            led.value(1)
        else:
            led.value(0)

    time.sleep(0.1)
