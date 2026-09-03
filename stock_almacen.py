herramientas = []
stock = []

for x in range(5):
    nombre = input("ingrese herramienta:".title())
    herramientas.append(nombre)
    numero = int(input("ingrese cantidad de stock:".title()))
    stock.append (numero)

print("lista sin ordenar:".title(), herramientas)
print("lista sin ordenar:".title(), stock) 
print("-" * 30)

for k in range(4):
    for x in range(4-k):
        if stock[x] > stock[x+1]:
            aux = stock[x]
            stock[x] = stock[x+1]
            stock[x+1] = aux

            aux1 = herramientas[x]
            herramientas[x] = herramientas[x+1]
            herramientas[x+1] = aux1

print("lista ordenada:".title(), herramientas)
print("lista ordenada:".title(), stock)
