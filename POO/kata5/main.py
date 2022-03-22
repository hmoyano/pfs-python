# Autor: Hector
# version: 0.0.1
# data: 15/03/2022

from POO.kata5.Usuario import Usuario
from POO.kata5.Alumno import Alumno

if __name__ == '__main__':

    # clase padre
    us1 = Usuario('Jose','Lopez')
    print(us1)
    us1.getName()

    #clase hija
    al1 = Alumno('Pepe','Perez','python')
    al1.getName()