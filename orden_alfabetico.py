def ordenar_cadenas(palabra1, palabra2):
    if palabra1 < palabra2:
        print(palabra1)
        print(palabra2)
    else:
        print(palabra2)
        print(palabra1)

def cargar_cadenas():
    texto1 = input("Ingrese palabra para ordenar: ")
    texto2 = input("Ingrese palabra para ordenar: ")
    ordenar_cadenas(texto1, texto2)


cargar_cadenas()
