amigos = []
numero = []

for x in range(5):
    nombre = input("ingrese nombre por favor:".title())
    amigos.append (nombre)
    valor = int(input("ingrese numero de telefono:".title()))
    numero.append (valor)

print("lista sin ordenar:".title(), amigos)
print("lista sin ordenar:".title(), numero)

for k in range(4):
    for x in range(4-k):
        if amigos[x] > amigos[x+1]:
            aux = amigos[x]
            amigos[x] = amigos[x+1]
            amigos[x+1] = aux

            aux2 = numero[x]
            numero[x] = numero[x+1]
            numero[x+1] = aux2

print("-" * 30)

for k in range(4):
    for x in range(4-k):
        if numero [x] > numero[x+1]:
            aux1 = numero[x]
            numero[x] = numero[x+1]
            numero[x+1] = aux1

            aux2 = amigos[x]
            amigos[x] = amigos[x+1]
            amigos[x+1] = aux2
            
print("lista ordenada:".title(), amigos)
print("lista ordenada:".title(), numero)
