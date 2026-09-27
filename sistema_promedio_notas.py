def procesar_notas(n1, n2, n3):
    promedio = (n1 + n2 + n3) / 3
    if promedio >= 7:
        print("Estado: Aprobado")
    else:
        print("Estado: Reprobado")

def cargar_notas():
    nota1 = int(input("Ingrese valor de nota: "))
    nota2 = int(input("Ingrese valor de nota: "))
    nota3 = int(input("Ingrese valor de nota: "))
    procesar_notas(nota1, nota2, nota3)


cargar_notas()
