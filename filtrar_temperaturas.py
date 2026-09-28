lista = []

for x in range(7):
    numero = int(input("Ingrese Numero: "))
    lista.append(numero)

print("Lista original de temperaturas:", lista)
posicion = 0

while posicion < len(lista):
    if lista[posicion] < 0:
        lista.pop(posicion)
    else:
        posicion = posicion + 1

print("Temperaturas filtradas (solo positivas):", lista)
