# Autor: Hector
# version: 0.0.1
# data: 15/03/2022

class Animal():
    # atributos de clase

    especie: str
    peso: float
    altura: float

    # atributos de instancia
    def __init__(self, newEsp):
        self.especie = newEsp
        self.peso = 15.7
        self.altura = 1.99

    # métodos

    def comer(self):
        pass

    def cazar(self):
        pass

    def dormir(self):
        pass

    def __str__(self):
        return f'{self.especie},{self.peso},{self.altura}'
