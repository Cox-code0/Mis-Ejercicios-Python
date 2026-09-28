lista = []

for x in range(5):
    edad = int(input("Ingrese Edad: "))
    lista.append(edad)

print("Edades cargadas:", lista)
print("-" * 30)
posicion = 0
menores = []

while posicion < len(lista):
    if lista[posicion] < 18:
        menores.append(lista.pop(posicion))
    else:
        posicion = posicion + 1

print("Lista de menores de edad aislados:", menores)
print("Lista final de mayores:", lista)
