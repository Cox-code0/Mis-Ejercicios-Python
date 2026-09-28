def perimetro(lado):
  produc = lado * 4
  return produc


medida_lado = int(input("Ingrese el valor del lado del cuadrado: "))

resultado_perimetro = perimetro(medida_lado)

print("El perimetro final del cuadrado es:", resultado_perimetro)
