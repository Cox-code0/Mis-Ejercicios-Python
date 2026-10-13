def cargar():
    diccionario = {}
    for x in range(2):
        jugador = input("Ingrese ID Del Usuario: ")
        continuar = "s"
        lista = []
        while continuar == "s":
            juego1 = input("Ingrese Juego Por Favor: ")
            horas = int(input("Ingrese Cantidad De Horas Jugadas: "))
            continuar = input("Desea Ingresar Otro Juego S|N Para Continuar: ")
            lista.append((juego1, horas))
        diccionario[jugador] = lista
    return diccionario 

def imprimir(diccionario):
    for elemento in diccionario:
        print(f"\n🎮 ID JUGADOR: {elemento}")
        print("--------------------")
        for juego, horas in diccionario[elemento]:
            print(f"🔹 Juego: {juego} | Horas: {horas}")

def determinar_consulta(diccionario):
    print("\n🔍 VENTANILLA DE CONSULTA")
    player = input("Ingrese ID a consultar: ")
    
    if player in diccionario:
        print(f"\n✅ Biblioteca de {player}:")
        for juego, horas in diccionario[player]:
            print(f" ➔ {juego}: {horas} hs")
    else:
        print("❌ El jugador no existe en el servidor, hermano.")


servidor = cargar()
imprimir(servidor)
determinar_consulta(servidor)
