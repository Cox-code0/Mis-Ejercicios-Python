producto = []
cantidad = []

for x in range(5):
    nombre = input("Ingrese Nombre Del Producto: ")
    producto.append(nombre)
    cant = int(input("Ingrese Cantidad De Dicho Producto: "))
    cantidad.append(cant)
    
print("Productos:", producto)
print("Cantidades:", cantidad)
posicion = 0

while posicion < len(cantidad):
    if cantidad[posicion] == 0:
        cantidad.pop(posicion)
        producto.pop(posicion)
    else:
        posicion = posicion + 1

print("Inventario activo (con stock):", producto)
print("Cantidades actualizadas:", cantidad)
