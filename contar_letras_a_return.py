def letra(cadena):
    conta = 0
    for x in range(len(cadena)):
        if cadena[x] in "aA":
            conta += 1
    return conta


palabra = input("ingrese palabra:".title())

resultado = letra(palabra)

print("la palabra es:", palabra, " tiene tantas letras a/A:", resultado)
