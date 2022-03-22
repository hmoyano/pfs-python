# Autor: Hector Moyano
# version: 0.0.1
# data: 15/03/2022

# description: kata II - sesión de clase

class Asignatura():
    # Atributos de clase
    nombre: str
    nota: int

    # Constructor de clase
    def __init__(self, newNombre):
        # Atributos de instancia
        self.nombre = newNombre
        self.nota: int

    # Métodos propios de clase - comportamiento
    # add nota
    def addNota(self, newNota):
        if 0 <= newNota <= 10:
            self.nota = newNota
        else:
            print('Introduce nota válida')

    # Método t string
    def __str__(self):
        return f"['{self.nombre}',{self.nota}]"