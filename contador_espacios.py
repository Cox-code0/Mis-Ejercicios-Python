def contar_espacios(texto):
    espacios = 0
    for x in range(len(texto)):
        if texto[x] == " ":
            espacios += 1
    print(espacios)


contar_espacios("hola mundo")
contar_espacios("aprendiendo python backend")
contar_espacios("sistema de gestion de bases de datos")
