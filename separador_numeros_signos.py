
lista = []

for x in range(8):
    numero = int(input("Ingrese numero por favor: "))
    lista.append(numero)

print("Lista original:", lista)
print("-" * 30)
posicion = 0
negativos = []

while posicion < len(lista):
    if lista[posicion] < 0:
        negativos.append(lista.pop(posicion))
    else:
        posicion = posicion + 1

print("Numeros negativos extraidos:", negativos)
print("Numeros positivos restantes:", lista)
