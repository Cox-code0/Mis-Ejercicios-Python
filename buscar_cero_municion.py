def buscar_cero(balas_cofres):
    for x in range(len(balas_cofres)):
        if balas_cofres[x] == 0:
            return "ALERTA : COFRE VACIO"
            
    return "ALERTA: TODO SEGURO"

balas_cofres = [30, 15, 0, 45, 8]

print("Estado de los cofres:", buscar_cero(balas_cofres))
