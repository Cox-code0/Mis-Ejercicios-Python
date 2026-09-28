def promedio(va1, va2, va3):
    resultado = (va1 + va2 + va3) / 3
    return resultado  

valor1 = int(input("Ingrese valor: "))
valor2 = int(input("Ingrese valor: "))
valor3 = int(input("Ingrese valor: "))

resultado_final = promedio(valor1, valor2, valor3)

print("El promedio obtenido es:", resultado_final)
