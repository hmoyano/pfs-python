# Autor: Hector Moyano
# version: 0.0.1
# data: 15/03/2022

# description: ejemplo de poo

class Clase():
    # atributos de clase
    profesor: str
    alumnos = []
    asignaturas = []

    # constructor de clase
    def __init__(self, newProf):
        self.profesor = newProf
        self.alumnos = []
        self.asignaturas = []

    # metodos propios
    def addAlum(self, newAlum):
        self.alumnos.append(newAlum)

    def delAlum(self, alum):
        self.alumnos.remove(alum)

    def addAsig(self, newAsign):
        self.asignaturas.append(newAsign)

    def delAsig(self, asign):
        self.asignaturas.remove(asign)