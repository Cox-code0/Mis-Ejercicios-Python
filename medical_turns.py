def cargar():
    diccionario = {}
    for x in range(2):
        matricula = int(input("Ingrese matricula: "))
        continuar = "s"
        lista = []
        while continuar == "s":
            nombre = input("Ingrese nombre del paciente: ")
            hora = int(input("Ingrese hora del turno: "))
            continuar = input("Desea cargar otro paciente s|n para continuar: ")
            lista.append((nombre, hora))
        diccionario[matricula] = lista
    return diccionario

def imprimir(diccionario):
    print("\n🏥 REPORTE DE MEDICOS Y GUARDIA:")
    print("==================================")
    for elemento in diccionario:
        print(f"\n📋 Matrícula de doctor: {elemento}")
        for nombre, hora in diccionario[elemento]:
            print(f"  👤 Paciente: {nombre} ➔ Hora del turno: {hora} hs")

def consultar(diccionario):
    print("\n🔍 VENTANILLA DE CONSULTA HOSPITALARIA")
    doctor = int(input("Ingrese matricula para consultar: "))

    if doctor in diccionario:
        print(f"\n✅ Agenda del Médico {doctor}:")
        for nombre, hora in diccionario[doctor]:
            print(f"  ➔ Paciente para atender: {nombre} | Turno: {hora} hs")
    else:
        print("❌ El profesional ingresado no se encuentra de guardia.")


guardia_hospital = cargar()
imprimir(guardia_hospital)
consultar(guardia_hospital)
