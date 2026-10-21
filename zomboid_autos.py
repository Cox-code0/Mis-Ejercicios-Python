class Vehiculo:
    def __init__(self, camioneta, defensa):
        self.camioneta = camioneta
        self.defensa = defensa
        self.vida = 100

    def accion(self, cargar):
        self.vida = self.vida - cargar

Personaje1 = Vehiculo("Shark", 40)
Personaje2 = Vehiculo("Robert", 20)

Personaje2.accion(Personaje1.defensa)
print(f"El campeon llamado {Personaje2.camioneta} recibio daño y le queda {Personaje2.vida}")
