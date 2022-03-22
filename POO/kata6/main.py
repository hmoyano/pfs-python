# Autor: Hector
# version: 0.0.1
# data: 15/03/2022

from POO.kata6.Animal import Animal
from POO.kata6.Mascota import Mascota
from POO.kata6.Perro import Perro

if __name__ == '__main__':
    # instacia de clase
    an1 = Animal('Perro')
    an2 = Animal('León')

    print(an1)

    masc1 = Mascota('Perry')
    print(masc1)
    print(masc1.nombre)

    p1 = Perro('Perro', 'Teckel', 'Kiara')
    print(p1)