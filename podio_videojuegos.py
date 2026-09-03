player = []
puntos = []

for x in range(5):
    nombres = input("ingrese nombre del jugador:".title())
    player.append (nombres)
    puntaje = int(input("ingrese puntaje del jugador:".title()))
    puntos.append (puntaje)


print("lista desordenada:".upper(), player)
print("lista desordenada:".upper(), puntos)
print("-" * 30)

for k in range(4):
    for x in range(4-k):
        if puntos[x] < puntos[x+1]:
            aux = puntos[x]
            puntos[x] = puntos[x+1]
            puntos[x+1] = aux

            aux2 = player[x]
            player[x] = player[x+1]
            player[x+1] = aux2

print("lista ordenada de mayor a menor:".upper(), player)
print("lista ordenada de mayor a menor:".upper(), puntos)
