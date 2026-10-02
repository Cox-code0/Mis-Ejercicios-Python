def cargar ():
    lista = []
    for x in range(10):
        valor1 = int(input("ingrese valores por favor:".title()))
        lista.append (valor1)
    return lista

def diferencia(lista):
    po = []
    ne = []
    for x in range(len(lista)):
        if lista[x] >= 0:
            po.append (lista[x])
        else:
            ne.append (lista[x])
    return po , ne


lista = cargar()
print("los numeros de la lista son:", lista)
print("-" * 30)
positivo,negativo= diferencia(lista)
print("los numeros positivos son:", positivo)
print("-" * 30)
print("los numeros negativos son:", negativo)
