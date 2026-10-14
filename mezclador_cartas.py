from random import  randint, shuffle 
def cargar():
    lista = []
    for x in range(5):
        lista.append ((randint(1,3)))
    return lista



def controlar (lista):
    while lista[0] != 1:
        shuffle(lista)


lista = cargar()
controlar(lista)
print(lista)
