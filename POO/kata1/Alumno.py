# Autor: Hector Moyano
# version: 0.0.1
# data: 15/03/2022

# description: kata I - sesión de clase

class Alumno():
    # Atributos de clase
    nombre: str
    apellidos: str
    dni: str
    edad: int
    notas = []

    # Constructor de clase
    def __init__(self, newNom, newApe, newDni, newEdad): # Atributos de instancia
        self.nombre = newNom
        self.apellidos = newApe
        self.dni = newDni
        self.edad = newEdad
        self.notas = []

    # Métodos de clase
    def saludar(self):
        print(f'Bienvenido {self.nombre}')

    def addNota(self, newNota):
        if 0 <= newNota <= 10:
            self.notas.append(newNota)
        else:
            print('Introduce nota valida')

    def addAge(self):
        self.edad += 1

    def getNotas(self):
        print(self.notas)

    # Metodo toString
    def __str__(self):
        return f'[{self.nombre}, {self.apellidos}, {self.edad}, {self.dni}, {self.notas}]'