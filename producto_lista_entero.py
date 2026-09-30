def producto(lista, entero):
    for x in range(len(lista)):
        resultado_multiplicacion = entero * lista[x]
        print(resultado_multiplicacion)

lista = [3, 7, 8, 10, 2]
entero = int(input("Ingrese entero para multiplicar: ".title()))

producto(lista, entero)
