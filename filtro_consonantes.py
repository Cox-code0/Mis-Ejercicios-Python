def contar_consonantes(texto):
    consonantes = 0
    for x in range(len(texto)):
        if texto[x] not in "aeiouAEIOU ":
            consonantes += 1
    print("Consonantes encontradas:", consonantes)


contonantes("Japon")
contonantes("Estados unidos")
contonantes("corea del sur")
