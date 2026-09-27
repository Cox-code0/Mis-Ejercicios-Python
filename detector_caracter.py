def contar_letra_a(texto):
    contador = 0
    for x in range(len(texto)):
        if texto[x] in "aA":
            contador += 1
    print("Cantidad total de letras A:", contador)

contar_letra_a("Alemania")
contar_letra_a("Abastecimiento")
contar_letra_a("Anticonstitucional")
