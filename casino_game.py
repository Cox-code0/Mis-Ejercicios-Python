import random

numero = random.randint(1,10)
continuar = "si"
conta = 0
while continuar == "si":
    jugador = int(input("ingrese un numero para adivinar:".title()))
    conta += 1
 
    if jugador == numero:
        print(f"felicidades ganaste, en estos intentos {conta}")
        continuar = "no"
       
        

    elif jugador < 1 or jugador > 10:
        print("numero no valido , tiene que ser entre 1 y 10")
