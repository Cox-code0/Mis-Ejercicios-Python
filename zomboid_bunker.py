class Superviviente:
    def __init__(self, nombre, profesion):
        self.nombre = nombre
        self.profesion = profesion
        self.vida = 100

personaje1 = Superviviente("Eduardo", "Ingeniero")
print(personaje1.nombre)
