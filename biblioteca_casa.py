libros = []
paginas = []

for x in range(5):
    name = input("ingrese nombre del libro:".title())
    libros.append (name)
    pages = int(input("ingrese cantidad de paginas:".title()))
    paginas.append (pages)

print("lista sin ordenar:".title(), libros)
print("lista sin ordenar:".title(), paginas)
print("-" * 30)

for k in range(4):
    for x in range(4-k):
        if libros[x] > libros[x+1]:
            aux = libros[x]
            libros[x] = libros[x+1]
            libros[x+1] = aux

            aux1 = paginas[x]
            paginas[x] = paginas[x+1]
            paginas[x+1] = aux1

for k in range(4):
    for x in range(4-k):
        if paginas[x] < paginas[x+1]:
            aux = paginas[x]
            paginas[x] = paginas[x+1]
            paginas[x+1] = aux

            aux1 = libros [x]
            libros[x] = libros[x+1]
            libros[x+1] = aux1

print("lista ordenada:".title(), libros)
print("lista ordenada:".title(), paginas)
