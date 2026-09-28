lista = []

for x in range(8):
    numero = int(input("Ingrese Numero: "))
    lista.append(numero)

print("Lista original:", lista)
posicion = 0

while posicion < len(lista):
    if lista[posicion] == 0:
        lista.pop(posicion)
    else:
        posicion = posicion + 1

print("Lista limpia (sin ceros):", lista)
