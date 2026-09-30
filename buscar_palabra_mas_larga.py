def largo(palabra):
    mayor = palabra[0]
    for x in range(len(palabra)):
        if len(palabra[x]) > len(mayor):
            mayor = palabra[x]
    return mayor

palabra = ["enero", "febrero", "marzo", "abril", "mayo", "junio"]

print("El caracter mas largo es:", largo(palabra))
