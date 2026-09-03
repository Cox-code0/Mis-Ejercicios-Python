empleado = []
edad = []

for x in range(5):
    nombre = input("ingrese nombre por favor:".title())
    empleado.append (nombre)
    valor = int(input("ingrese edad por favor:".title()))
    edad.append (valor)

print("lista sin ordenar:".upper(), empleado)
print("lista sin ordenar:".upper(), edad)
print("-" * 30)
for k in range(4):
    for x in range(4-k):
        if edad[x] < edad[x+1]:
            aux = edad[x]
            edad[x] = edad[x+1]
            edad [x+1] = aux

            aux2 = empleado [x]
            empleado [x] = empleado[x+1]
            empleado[x+1] = aux2

print("lista ordenada de mayor a menor:".upper(), empleado)
print("lista ordenada de mayor a menor:".upper(), edad)
