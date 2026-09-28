

lista = []

for x in range(10):
    letras = input("Ingrese Letras: ")
    lista.append(letras)

print("Lista original de caracteres:", lista)
posicion = 0
vocales = []

while posicion < len(lista):
    caracter = lista[posicion].lower()
    if caracter == "a" or caracter == "e" or caracter == "i" or caracter == "o" or caracter == "u":
        vocales.append(lista.pop(posicion))
    else:
        posicion = posicion + 1

print("Vocales aisladas:", vocales)
print("Consonantes/caracteres restantes:", lista)
