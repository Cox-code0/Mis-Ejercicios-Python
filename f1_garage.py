class AutoF1:
    def __init__(self, piloto, escuderia):
        self.piloto = piloto
        self.escuderia = escuderia
        self.combustible = 100

    def correr(self):
        print("¡El auto está en pista gastando nafta!")
        self.combustible = self.combustible - 10

auto1 = AutoF1("Kane", "Japon")
auto2 = AutoF1("Rofelt", "Peru")

auto1.correr()
print(f"Combustible auto 1: {auto1.combustible}")
print(f"Combustible auto 2: {auto2.combustible}")
