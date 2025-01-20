import dht
import machine
import time

dht_pin = machine.Pin(0)
sensor = dht.DHT11(dht_pin)

while True:
    try:
        # Atualiza a leitura do sensor
        sensor.measure()
        
        # Obtém temperatura e umidade
        temperatura = sensor.temperature()
        umidade = sensor.humidity()
        
        # Exibe os dados no console
        print(f"Temperatura: {temperatura}C")
        print(f"Umidade: {umidade}%")
        
    except OSError as e:
        print("Erro ao ler o sensor:", e)
    
    # Aguarda 2 segundos antes de nova leitura
    time.sleep(2)
