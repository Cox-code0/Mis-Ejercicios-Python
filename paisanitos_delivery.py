def cargar():
    diccionario = {}
    for x in range(3):
        camion = int(input("Ingrese número de camion: "))
        lista = []
        continuar = "s"
        while continuar == "s":
            corte = input("Ingrese corte de pollo: ")
            kilos = int(input("Ingrese kilos del corte: "))
            continuar = input("Desea cargar mas cortes s|n para continuar: ")
            lista.append((corte, kilos))
        diccionario[camion] = lista
    return diccionario

def imprimir(diccionario):
    print("\n🚚 CAMIONES Y SU MERCADERÍA:")
    print("==============================")
    for elemento in diccionario:
        print(f"\n🚛 Camión N°: {elemento}")
        for corte, kilos in diccionario[elemento]:
            print(f"  ➔ Corte: {corte} | Kilos: {kilos} kg")

def deposito(diccionario):
    print("\n🔍 CONTROL DE DEPÓSITO")
    camion = int(input("Ingrese numero de camion para controlar: "))
    if camion in diccionario:
        print(f"\n✅ Datos del Camión {camion}:")
        for corte, kilos in diccionario[camion]:
            print(f"  🔹 {corte}: {kilos} kg")
    else:
        print("❌ El camión ingresado no está programado en la hoja de ruta.")


diccionario_stock = cargar()
imprimir(diccionario_stock)
deposito(diccionario_stock)
