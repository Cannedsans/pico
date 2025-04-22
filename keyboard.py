from machine import Pin
from time import sleep
# Definir os pinos das linhas e colunas
linhas = [Pin(0, Pin.OUT), Pin(1, Pin.OUT), Pin(2, Pin.OUT), Pin(3, Pin.OUT)]
colunas = [Pin(4, Pin.IN, Pin.PULL_DOWN), Pin(5, Pin.IN, Pin.PULL_DOWN), Pin(6, Pin.IN, Pin.PULL_DOWN), Pin(7, Pin.IN, Pin.PULL_DOWN)]

# Definir a matriz do teclado
matrix = [
    ['+', '9', '8', '7'],
    ['-', '4', '5', '6'],
    ['/', '1', '2', '3'],
    ['*', 'del', '0', '*']
]

# Função para ler o teclado matricial
def ler_teclado():
    for i, linha in enumerate(linhas):
        linha.value(1)  # Ativar a linha
        for j, coluna in enumerate(colunas):
            if coluna.value() == 1:  # Verificar se a coluna está ativa
                linha.value(0)  # Desativar a linha antes de retornar
                return matrix[i][j]
        linha.value(0)  # Desativar a linha após verificar todas as colunas
    return None

# Exemplo de uso
while True:
    tecla = ler_teclado()
    if tecla:
        print(f"Tecla pressionada: {tecla}")
        sleep(0.5)