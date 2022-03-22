# Autor: Hector
# version: 0.0.1
# data: 15/03/2022

from POO.kata5.Usuario import Usuario

class Alumno(Usuario):
    # atributos de clase
    asignatura: str

    # atributos de instancia
    def __init__(self, newNom, newApe, newAsig):
        super().__init__(newNom, newApe)
        self.asignatura = newAsig

    #metodos propios

    def getName(self):
        print(f'Bienvenido {self.nombre} {self.apellido} {self.asignatura}')
