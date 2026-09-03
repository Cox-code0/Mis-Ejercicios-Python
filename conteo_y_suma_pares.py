valores_negativos = 0
valores_positivos = 0
multiplo15 = 0
pares = 0
for x in range(1,11):
    valor = int ( input("ingrese valor:"))
    if valor < 0:
        valores_negativos = valores_negativos + 1
    if valor > 0:
        valores_positivos = valores_positivos + 1
    if valor %15==0:
        multiplo15 = multiplo15 + 1
    if valor % 2 == 0:
        pares = pares + valor
print("la cantidad de valores negativos son:", valores_negativos)
print("la cantidad de valores positivos son:", valores_positivos)
print("la cantidad de multiplos de 15 son:", multiplo15)
print("el valor acumulado de los números pares ingresados es:", pares)
