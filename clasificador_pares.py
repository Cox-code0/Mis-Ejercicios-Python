def verificar_numeros_pares(v1, v2, v3):
    conteo_pares = 0
    if v1 % 2 == 0:
        conteo_pares += 1
    if v2 % 2 == 0:
        conteo_pares += 1
    if v3 % 2 == 0:
        conteo_pares += 1
    print("Cantidad total de numeros pares:", conteo_pares)

def cargar_enteros():
    valor1 = int(input("Ingrese valor entero: "))
    valor2 = int(input("Ingrese valor entero: "))
    valor3 = int(input("Ingrese valor entero: "))
    verificar_numeros_pares(valor1, valor2, valor3)

cargar_enteros()
