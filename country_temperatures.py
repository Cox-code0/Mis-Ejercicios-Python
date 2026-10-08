def cargar():
    paises = []
    for x in range(4):
        country = input("ingrese nombre del country:".title())
        temperature = int(input("ingrese temperature del country:".title()))
        paises.append((country, temperature))
    return(paises)

def temperatura(paises):
    pos = 0
    for x in range(len(paises)):
        if paises[x][1] > paises[pos][1]:
            pos = x
    print("el country con mayor temperature es:", paises[pos][0])


paises = cargar()
temperatura(paises)
