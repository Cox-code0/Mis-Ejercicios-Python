alumnos = []
notas = []

for x in range(6):
    name = input("Ingrese Nombre Del Alumno: ")
    alumnos.append(name)
    note = int(input("Ingrese Nota Del Alumno: "))
    notas.append(note)

print("Alumnos cargados:", alumnos)
print("Notas cargadas:", notas)
print("-" * 30)
posicion = 0

while posicion < len(notas):
    if notas[posicion] < 4:
        alumnos.pop(posicion)
        notas.pop(posicion)
    else:
        posicion = posicion + 1

print("Alumnos que continuan en carrera:", alumnos)
print("Notas aprobadas:", notas)
