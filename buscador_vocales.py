def analizar_vocales(texto):
    conta_a = 0
    conta_e = 0
    for x in range(len(texto)):
        if texto[x].lower() == "a":
            conta_a += 1
        if texto[x].lower() == "e":
            conta_e += 1
    print("Cantidad de letras A:", conta_a)
    print("Cantidad de letras E:", conta_e)


analizar_vocales("cocinar")
analizar_vocales("gastronomia")
analizar_vocales("independiente")
