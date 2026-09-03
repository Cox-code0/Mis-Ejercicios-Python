producto = []
precio = []

for x in range(5):
    nombre = input("ingrese nombre del producto:".title())
    producto.append (nombre)
    valor = int(input("ingrese valor del producto:".title()))
    precio.append (valor)


print("lista sin ordenar:".upper(), producto)
print("lista sin ordenar:".upper(), precio)
print("-" * 30)

for k in range(4):
    for x in range(4-k):
        if precio[x] > precio [x+1]:
            aux = precio [x]
            precio[x] = precio[x+1]
            precio[x+1] = aux

            aux2 = producto[x]
            producto[x] = producto[x+1]
            producto[x+1] = aux2

print("lista ordenada:".upper(), producto)
print("lista ordenada:".upper(), precio)
