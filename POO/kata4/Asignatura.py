# Autor: Hector
# version: 0.0.1
# data: 15/03/2022

# description: kata IV - sesión de clase

class Asignatura():
    # Atributos de clase
    __id: str
    nombre: str
    __nota: int

    # Constructor de clase
    def __init__(self, newNombre):
        # Atributos de instancia
        self.__id: str
        self.nombre = newNombre
        self.__nota: int

    # Métodos propios de clase - comportamiento
    # add nota
    def addNota(self, newNota):
        if 0 <= newNota <= 10:
            self.__nota = newNota
        else:
            print('Introduce nota válida')

    # Método t string
    def __str__(self):
        return f"['{self.nombre}',{self.__nota}]"

    # getters & setters
    @property
    def id(self):
        return self.__id

    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def set_nota(self, newNota):
        self.__nota = newNota