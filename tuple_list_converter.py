def modificar_tupla(numeros):
    modificada = list(numeros)
    modificada.append(100)
    modificada1 = tuple(modificada)
    return(modificada1)
    

numeros = (10, 20, 30, 40, 50)
modificacion = modificar_tupla(numeros)
print(modificacion)
