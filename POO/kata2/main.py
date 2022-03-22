# Autor: Hector Moyano
# version: 0.0.1
# data: 15/03/2022

# description: kata II - sesión de clase

from POO.kata2.Alumno import Alumno
from POO.kata2.Asignatura import Asignatura

if __name__ == '__main__':
    # Instancias de clase
    al1 = Alumno('Jose', 'Marín', '123456789A', 35)

    # Uso de metodos de clase
    al1.addNota(9)
    al1.addNota(5)
    al1.addNota(7)
    al1.addAge()

    # Instancia de Asignatura
    as1 = Asignatura('ciencias')
    as1.addNota(10)

    as2 = Asignatura('literatura')
    as2.addNota(7)

    as3 = Asignatura('python')
    as3.addNota(7)

    # Pasamos en objeto asignatura por composición al objeto alumno
    al1.addAsignatura(as1)
    al1.addAsignatura(as2)

    print(al1)