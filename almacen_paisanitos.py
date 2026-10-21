class Camion:
    def __init__(self, numero, chofer):
        self.numero = numero
        self.chofer = chofer
        self.kilos_totales = 0

    def cargar_pollos(self, kilos):
        self.kilos_totales = self.kilos_totales + kilos

camion1 = Camion(101, "Sharon")
camion1.cargar_pollos(150)
camion1.cargar_pollos(220)
print(f"El camion {camion1.numero} de {camion1.chofer} lleva {camion1.kilos_totales} kilos totales.")
