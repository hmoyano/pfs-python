# Auth: Hector Moyano
# Version: 0.0.1
# data: 15/03/2022

class Persona():
    # Atributos de clase
    nombre: str
    apellidos = 'Porras'
    edad = 0
    email = 'pepe@gmail.com'

    # Constructor de clase
    def __init__(self, newname, newsurname, newedad):
        self.nombre = newname
        self.apellidos = newsurname
        self.edad = newedad



    # Comportamiento = métodos de clase
    def Saludar(self):
        print(f'Bienvenido {self.nombre}')
