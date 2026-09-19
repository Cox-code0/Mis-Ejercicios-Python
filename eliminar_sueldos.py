empleados = []
sueldos = []
sub = int(input("cuantos empleados tiene la empresa:".title()))

for x in range(sub):
    nombre = input("ingrese nombre del empleado:".title())
    empleados.append (nombre)
    sueldo = int(input("ingrese sueldo del empleado:".title()))
    sueldos.append (sueldo)
    
print(empleados)
print(sueldos)
print("-" * 30)

posicion = 0

while posicion < len(sueldos):
    if sueldos[posicion]>10000:
        sueldos.pop (posicion)
        empleados.pop (posicion)
    else:
        posicion = posicion + 1

print(empleados)
print(sueldos)

