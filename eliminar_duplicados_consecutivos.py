lista = []

for x in range(8):
    number = int(input("Ingrese Numero: "))
    lista.append(number)

print("Lista original con duplicados:", lista)
posicion = 0

while posicion < len(lista) - 1:
    if lista[posicion] == lista[posicion + 1]:
        lista.pop(posicion)
    else:
        posicion = posicion + 1

print("Lista final sin repetidos consecutivos:", lista)
