# Auth: Hector Moyano
# Version: 0.0.1
# data: 15/03/2022
# KATA 3

class Clase():

    # atributos de clase

    __id: str
    profesor: str
    alumnos = []
    asignaturas = []

    # constructor de clase

    def __init__(self, newid, profesor):
        self.profesor = profesor
        self.alumnos = []
        self.asignaturas = []
        self.__id = newid


    # métodos

    def addAlumno(self, newAlumno):
        self.alumnos.append(newAlumno)
    def delAlumno(self, alum):
        self.alumnos.remove(alum)
    def addAsig(self, newAsig):
        self.asignaturas.append(newAsig)
    def delAsig(self, asig):
        self.asignaturas.remove(asig)