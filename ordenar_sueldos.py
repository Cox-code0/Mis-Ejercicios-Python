empleados = int(input("ingrese cantidad de empleados:".title()))

sueldo = []


for x in range(1, empleados + 1):
    valor = int(input("ingrese sueldo:"))
    sueldo.append (valor)

print("sueldos sin ordenar:", sueldo)
for k in range(empleados - 1):
    for x in range(empleados - 1 - k):
        if sueldo[x] > sueldo[x+1]:
            aux = sueldo[x]
            sueldo[x] = sueldo[x+1]
            sueldo[x+1] = aux

print("sueldos ordenados de menor a mayor:", sueldo)
