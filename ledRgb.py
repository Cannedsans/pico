from machine import Pin

r = Pin(2, Pin.OUT)
g = Pin(0, Pin.OUT)
b = Pin(1, Pin.OUT)

while True:
    cor = input("Digite r, g ou b: ").strip().lower()

    if cor == 'r':
        r.toggle()
    elif cor == 'g':
        g.toggle()
    elif cor == 'b':
        b.toggle()
    else:
        print("Dado inválido")