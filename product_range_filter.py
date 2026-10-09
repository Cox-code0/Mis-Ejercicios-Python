def cargar():
    lista = []
    for x in range(5):
        producto = input("ingrese nombre del producto:".title())
        precio = int(input("ingrese precio del producto:".title()))
        lista.append((producto, precio))
    return lista


def listar_todos(medio):
    print("\n--- Lista Completa de Productos ---")
  
    for elemento in medio:
        print(f"Producto: {elemento[0]} | Precio: {elemento[1]}")


def comprendido(medio):
    lista1 = []
    for elemento in medio:
        if elemento[1] >= 10 and elemento[1] <= 15:
            lista1.append(elemento)
    return lista1



medio = cargar()


listar_todos(medio) 

print("\n--- Productos entre 10 y 15 ---")
comprendido1 = comprendido(medio)
print(comprendido1)
