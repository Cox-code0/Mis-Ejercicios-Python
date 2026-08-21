tiempo = []

for x in range(5):
    valor = int(input("ingrese tiempo del corredor:".title()))
    tiempo.append (valor)
print("-" * 30)
print("lista sin ordenar:".title(), tiempo)
print("-" * 30)

for k in range(4):
    for x in range(4-k):
        if tiempo[x] > tiempo[x+1]:
            aux = tiempo[x]
            tiempo[x] = tiempo[x+1]
            tiempo[x+1] = aux
            
print("lista ordenada:".title(), tiempo)
print("-" * 30)
print("y la medalla de oro es para:".upper(), tiempo[0])
print("-" * 30)
print("y la medalla de plata es para:".upper(), tiempo[1])
print("-" * 30)
print("y la medalla de bronce es para:".upper(), tiempo[2])
print("-" * 30)
print("¡¡felicidades, muchas gracias por competir!!".upper())
    

    

    
    
