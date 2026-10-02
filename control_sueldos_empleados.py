def cargar():
    sueldos = []
    for x in range(10):
        sueldo = int(input("ingrese sueldo por favor:"))
        sueldos.append (sueldo)
    return sueldos

def superior (sueldo):
    conta = 0
    for x in range(len(sueldo)):
        if sueldo[x] > 4000:
            conta += 1
    return conta

def promedio (sueldo):
    suma = 0
    for x in range(len(sueldo)):
        suma = suma + sueldo[x]
    promedio = suma // 10
    return promedio

def bajo_promedio (sueldo):
    li = []
    for x in range(len(sueldo)):
        if sueldo[x] < promedio:
            li.append (sueldo[x])
    return li
        

sueldo = cargar()
print("los sueldos de los empleados es:", sueldo)
print("-" * 30)
superior = superior(sueldo)
print("los sueldos superiores a 4000 son:", superior)
print("-" * 30)
promedio = promedio(sueldo)
print("el promedio de los sueldo es:", promedio)
print("-" * 30)
li = bajo_promedio(sueldo)
print("todos los sueldos bajo del promedio son:", li)
print("-" * 30)
