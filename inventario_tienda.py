
producto = []
precio = []

for x in range(4):
    nombre = input("ingrese nombre del prodcuto:".title())
    print("-" * 30)
    producto.append (nombre)
    valor = int(input("ingrese precio del producto:".title()))
    print("-" * 30)
    precio.append (valor)

mayor = precio[0]
nombre = producto [0]

for x in range(4):
    if precio[x] > mayor:
        mayor = precio[x]
        nombre = producto [x]

print("la lista de los producto es:", producto)
print("-" * 30)
print("los precios de los productos son:", precio)
print("-" * 30)
print("el producto mas caro es".title(), nombre, "y cuesta $".title(), mayor)
