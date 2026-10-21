class Arma:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cargador = 0

    def cargar(self, cargar):
        self.cargador = self.cargador + cargar

Armamento = Arma("M16")
print(f"el arma {Armamento.nombre} tiene esta cantidad de balas {Armamento.cargador}")
print("recargando arma".upper())
Armamento.cargar(15)
print(f"el arma {Armamento.nombre} tiene esta cantidad de balas {Armamento.cargador}")
print("regargando arma".upper())
Armamento.cargar(15)
print(f"el arma {Armamento.nombre} tiene esta cantidad de balas {Armamento.cargador}")
