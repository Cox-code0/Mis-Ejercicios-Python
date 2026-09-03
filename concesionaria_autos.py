modelo = []
velocidad = []

for x in range(5):
    nombre = input("ingrese modelo del auto:".title())
    modelo.append (nombre)
    speed = int(input("ingrese velocidad del auto:").title())
    velocidad.append (speed)

print("lista sin ordenar:".title(), modelo)
print("lista sin ordenar:".title(), velocidad)
print("-" * 30)

for k in range(4):
    for x in range(4-k):
        if modelo[x] > modelo[x+1]:
            aux = modelo[x]
            modelo[x] = modelo[x+1]
            modelo[x+1] = aux

            aux1 = velocidad[x]
            velocidad[x] = velocidad[x+1]
            velocidad[x+1] = aux1

for k in range(4):
    for x in range(4-k):
        if velocidad[x] < velocidad[x+1]:
            aux = velocidad[x]
            velocidad[x] = velocidad[x+1]
            velocidad[x+1] = aux

            aux1 = modelo[x]
            modelo[x] = modelo[x+1]
            modelo[x+1] = aux1

print("lista ordenada:".title(), modelo)
print("lista ordenada:".title(), velocidad)
