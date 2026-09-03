corredores = []
tiempo = []

for x in range(5):
    nombre = input("ingrese nombre del corredor:".title())
    corredores.append (nombre)
    time = int(input("ingrese tiempo del corredor:".title()))
    tiempo.append(time)

print("lista sin ordenar:".title(), corredores)
print("lista sin ordenar:".title(), tiempo)
print("-" * 30)

for k in range(4):
    for x in range(4-k):
        if corredores [x] > corredores[x+1]:
            aux = corredores[x]
            corredores[x] = corredores[x+1]
            corredores[x+1] = aux

            aux1 = tiempo[x]
            tiempo[x] = tiempo[x+1]
            tiempo[x+1] = aux1

for k in range(4):
    for x in range(4-k):
        if tiempo[x] > tiempo[x+1]:
            aux = tiempo[x]
            tiempo[x] = tiempo[x+1]
            tiempo[x+1] = aux

            aux1 = corredores[x]
            corredores[x] = corredores[x+1]
            corredores[x+1] = aux1
            
print("lista ordenada:".title(), corredores)
print("lista ordenada:".title(), tiempo)
