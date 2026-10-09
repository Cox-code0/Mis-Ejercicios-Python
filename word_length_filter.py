def cargar():
    lista = []
    for x in range(5):
        palabra = input("ingrese palabra por favor:".title())
        lista.append(palabra)
    return lista


def mayor_palabra(mayor):
    lista1 = []

    for elemento in mayor:
        if len(elemento) > 5:
            lista1.append(elemento)
    return lista1

    

mayor = cargar()
print("\n--- Palabras con más de 5 caracteres ---")
print(mayor_palabra(mayor))
