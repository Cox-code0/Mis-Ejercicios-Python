def superficie(lado1,lado2):
    resultado1 = lado1 * lado2
    return resultado1


valor1 = int(input("ingrese base del rectangulo:".title()))
valor2 = int(input("ingrese altura del rectangulo:".title()))
resultado1 = superficie(valor1,valor2)
print(resultado1)
valor1 = int(input("ingrese base del rectangulo:".title()))
valor2 = int(input("ingrese altura del rectangulo:".title()))
resultado2 = superficie(valor1,valor2)
print(resultado2)

if resultado1 == resultado2:
    print("los rectangulo tienen la misma superficie:", resultado1,"//",resultado2)
else:
    if resultado1 > resultado2:
        print("superficie mayor es:", resultado1)
    else:
        print("resultado mayor es:", resultado2)
