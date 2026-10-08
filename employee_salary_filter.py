
def cargar():
    lista = []
    for x in range(5):
        empleado = input("ingrese nombre del empleado:".title())
        sueldo = int(input("ingrese sueldo del empleado:".title()))
        lista.append((empleado,sueldo))
    return (lista)

def mayor_sueldo (sueldo):
    print("los empleados que cobran mas de 4000 son:")
    for x in range(len(sueldo)):
        if sueldo[x][1] > 4000:
            print(sueldo[x][0])

sueldo = cargar()
mayor_sueldo (sueldo)
