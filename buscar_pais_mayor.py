pais = []

for x in range(5):
    name = input("ingrese nombre del pais:".title())
    pais.append(name)


print("la lista de los paises sin ordenar es:", pais)


for x in range(4):
    if pais[x] > pais[x+1]:
        aux = pais[x]
        pais[x] = pais[x+1]
        pais [x+1] = aux

print("el pais mayor alfabeticamente es:".upper(), pais[4])
