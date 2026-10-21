class Auto:
    def __init__(self, patente):
        self.patente = patente
        self.lista = []

    def destinos(self, cargar):
        self.lista.append(cargar)

Camioneta = Auto(891230)
Camioneta.destinos("Japan")
Camioneta.destinos("USA")
Camioneta.destinos("China")
print(f"la camioneta {Camioneta.patente} tiene estos destinos pendientes {Camioneta.lista}")
