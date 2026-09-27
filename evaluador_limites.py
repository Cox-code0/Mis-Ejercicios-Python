def evaluar_limites(num1, num2):
    if num1 > num2:
        print("El valor mayor es:", num1)
        print("El valor menor es:", num2)
    else:
        print("El valor mayor es:", num2)
        print("El valor menor es:", num1)

def cargar_datos():
    val1 = int(input("Ingrese primer numero entero: "))
    val2 = int(input("Ingrese segundo numero entero: "))
    evaluar_limites(val1, val2)


cargar_datos()
