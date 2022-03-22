# Autor: Hector
# version: 0.0.1
# data: 15/03/2022

# description: kata IV - sesión de clase

class Clase():
    # atributos de clase
    # __id: str
    profesor: str
    alumnos = []
    asignaturas = []

    # constructor de clase
    def __init__(self, newId, newProf):
        self.__id = newId
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

    # getters & setters
    # def get_id(self):
    #     return self.__id
    #
    # def set_id(self, newId):
    #     self.__id = newId

    @property
    def id(self):
        return self.__id

    # @id.setter
    # def set_dinero(self, newId):
    #     self.__id = newId