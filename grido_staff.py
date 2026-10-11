def cargar():
    empleados = {}
    for x in range(3):
        legajo = int(input("Ingrese número de legajo: ".title()))
        nombre = input("Ingrese nombre completo por favor: ".title())
        empleados[legajo] = nombre
    return empleados

def imprimir(lista):
    print("\n==============================================")
    print("📊 LISTADO OFICIAL DE PERSONAL - GRIDO HELADOS")
    print("==============================================")
    for elemento in lista:
        print(f"👤 Legajo N° {elemento} | Pertenece a: {lista[elemento]}")


lista = cargar()
imprimir(lista)
