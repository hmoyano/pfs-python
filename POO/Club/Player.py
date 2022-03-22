# Auth: Hector Moyano
# Version: 0.0.1
# data: 15/03/2022

class Player():
    # Atributos de clase
    nombre: str
    edad: int
    rol: str

    # Constructor de clase
    def __init__(self, nombre, edad, rol):
        self.nombre = nombre
        self.edad = edad
        self.rol = rol

    # Métodos de clase - comportamiento
    def saluda(self):
        print(f'Bienvenido {self.nombre}')