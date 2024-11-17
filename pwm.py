from machine import ADC, Pin, PWM
from time import sleep

# Configura o pino do ADC e do PWM
potenciometro = ADC(27)  # Se estiver usando Raspberry Pi Pico, use: ADC(Pin(27))
saida = PWM(Pin(15))
saida.freq(1000)  # Define a frequência do PWM

while True:
    # Lê o valor do potenciômetro (0 a 65535)
    valor_adc = potenciometro.read_u16()
    
    # Define o duty cycle do PWM com base no valor lido
    saida.duty_u16(valor_adc)
    
    # Adiciona um pequeno delay para evitar sobrecarga
    sleep(0.01)
