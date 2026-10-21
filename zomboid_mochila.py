class Superviviente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mochila = []

    def juntar_item(self, objetos):
        item = ("hacha", "machete")
        self.mochila.append(item)

personaje = Superviviente("Shane")
personaje.juntar_item("comida")
print(f"el superviviente es {personaje.nombre} y recogio {personaje.mochila}")
