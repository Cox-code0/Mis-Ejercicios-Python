cliente = []
dinero = []

for x in range(5):
    nombre = input("ingrese nombre del cliente:".title())
    cliente.append (nombre)
    valor = int(input("ingrese dinero que invirtio:".title()))
    dinero.append (valor)

print("lista sin ordenar:".title(), cliente)
print("lista sin ordenar:".title(), dinero)
print("-" * 30)
for k in range(4):
    for x in range(4-k):
        if cliente[x] > cliente[x+1]:
            aux = cliente[x]
            cliente[x] = cliente[x+1]
            cliente[x+1] = aux

            aux1 = dinero [x]
            dinero[x] = dinero[x+1]
            dinero[x+1] = aux1

for k in range(4):
    for x in range(4-k):
        if dinero[x] < dinero[x+1]:
            aux = dinero[x]
            dinero[x] = dinero[x+1]
            dinero[x+1] = aux

            aux1 = cliente[x]
            cliente[x] = cliente[x+1]
            cliente[x+1] = aux1

print("lista ordenada:".title(), cliente)
print("lista ordenada:".title(), dinero)
