nombre = []
nota = []

for x in range(6):
    alumno = input("Ingrese nombre por favor: ".title())
    nombre.append(alumno)
    valor = int(input("Ingrese nota por favor: ".title()))
    nota.append(valor)

aprobado = 0
reprobado = []

for x in range(6):
    if nota[x] >= 6:
        aprobado += 1
    else:
        reprobado.append(nombre[x])
        
print("La cantidad de alumnos que aprobaron fueron: ".title(), aprobado)
print("-" * 30)
print("Los alumnos que desaprobaron son: ".title(), reprobado)
