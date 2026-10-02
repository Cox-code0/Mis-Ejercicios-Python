def cargar():
    arti = []
    precios = []
    for x in range(5):
        valor1 = input("ingrese nombre del articulo:")
        arti.append(valor1)
        valor2 = int(input("ingrese precio del articulo:"))
        precios.append (valor2)
    return arti , precios

def mayor (arti,precios):
    ma = precios[0]
    art = arti[0]
    for x in range (len(precios)):
        if precios[x] > ma:
            ma = precios[x]
            art = arti[x]
    return art , ma
    
def importe (precios,arti):
    money = int(input("ingrese importe:"))
    li = []
    for x in range(len(precios)):
        if precios[x] <= money:
            li.append (arti[x])
    return li


arti,precios = cargar()
print(arti)
print(precios)
print("-" * 30)
articulo_mayor = mayor(arti,precios)
print("el articulo mayor es:", articulo_mayor)
print("-" * 30)
money = importe(precios,arti)
print("-" * 30)
print("y los productos que puede comprar con el importe que ingreso son:")
print(money)
