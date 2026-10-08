def cargar():
    game = input("ingrese nombre del videojuego:".title())
    buy = int(input("ingrese precio del videojuego:".title()))
    return (game, buy)

def recibir(juego):
    va1, va2 = juego
    print("el juego elegido es:", va1, "y cuesta: $", va2)


juego = cargar()
recibir(juego)
