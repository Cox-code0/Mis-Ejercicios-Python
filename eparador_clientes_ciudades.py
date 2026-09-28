clientes = []
paises = []

for x in range(5):
    customers = input("Ingrese Nombre Del Cliente: ")
    clientes.append(customers)
    country = input("Ingrese Nombre Del Pais: ")
    paises.append(country)

print("Clientes cargados:", clientes)
print("Paises cargados:", paises)
print("-" * 30)

clientes_internacionales = []
paises_filtrados = []
posicion = 0

while posicion < len(paises):
    if paises[posicion].lower() == "japon":
         clientes_internacionales.append(clientes.pop(posicion))
         paises_filtrados.append(paises.pop(posicion))
    else:
        posicion = posicion + 1

print("Clientes de Japon aislados:", clientes_internacionales)
print("Paises confirmados:", paises_filtrados)
