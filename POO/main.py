# Auth: Hector Moyano
# Version: 0.0.1
# data: 02/03/2022

from POO.Class.Asignatura import Asignatura
from POO.Class.Alumno import Alumno
from POO.Class.Clase import Clase

if __name__ == '__main__':
    as1 = Asignatura('ciencias')
    as1.addNota(10)

    as2 = Asignatura('matematicas')
    as2.addNota(8)

    # print(as1)
    # print(as1.nombre)
    # print(as1.nota)

    # print(as2)
    # print(as2.nombre)
    # print(as2.nota)
    #
    al1 = Alumno()
    # al1.addAsignatura(as1)
    # al1.addAsignatura(as2)
    #
    # al1.getAsig()
    #
    # al1.delAsignatura(as1)
    #
    # al1.getAsig()

    cl1 = Clase('21','Manuel')
    print(cl1.profesor)

    cl1.addAsig(as1)
    cl1.addAsig(as2)
    print('Listado de asignaturas ----------------------------')

    for asig in cl1.asignaturas:
        print(asig)

    cl1.addAlumno(al1)
    print('Listado de alumnos -----------------------')

    for alum in cl1.alumnos:
        print(alum)

    cl2 = Clase('23','Manolo')
    print(cl2.profesor)