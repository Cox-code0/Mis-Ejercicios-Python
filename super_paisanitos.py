class Almacen:
    def __init__(self, nombre):
        self.nombre = nombre
        self.pagar = 0

    def sumar(self, cargar):
        self.pagar = self.pagar + cargar

cliente = Almacen("Randal")
cliente.sumar(150)
cliente.sumar(230)
cliente.sumar(500)
print(f"El cliente {cliente.nombre} debe abonar en total = {cliente.pagar}")
