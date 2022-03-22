# Autor: Hector
# version: 0.0.1
# data: 15/03/2022

from POO.kata6.Animal import Animal
from POO.kata6.Mascota import Mascota

class Perro(Animal,Mascota):

    raza: str

    def __init__(self, newRaza, newEsp, newNom):
        Animal.__init__(self, newEsp)
        Mascota.__init__(self, newNom)
        self.raza = newRaza

    def saluda(self):
        print('Hola guau')

    def __str__(self):
        return f'[{self.especie}, {self.nombre}, {self.raza}]'

