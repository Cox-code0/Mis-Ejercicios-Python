lista = []
lista1= []

for x in range(5):
    pais = input("ingrese pais por favor:".title())
    lista.append (pais)
    valor = int(input("ingrese temperatura:".title()))
    lista1.append (valor)

print("lista sin ordenar:".title(), lista)
print("lista sin ordenar:".title(), lista1)

for k in range(4):
    for x in range(4-k):
        if lista1[x] > lista1[x+1]:
            aux = lista1[x]
            lista1[x] = lista1[x+1]
            lista1[x+1] = aux

            aux1 = lista[x]
            lista[x] = lista[x+1]
            lista[x+1] = aux1

print("lista ordenada:".title(), lista)
print("lista ordenada:".title(), lista1)
