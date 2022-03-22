# Auth: Hector Moyano
# Version: 0.0.1
# data: 15/03/2022
# KATA I: Evaluación de Alumnos

class Alumno():
    #Atributos de clase
    nombre: str = 'Jose'
    apellidos: str
    dni: str
    edad: int
    nota = []
    asignaturas = []

    #Constructor de clase
    def __init__(self):
        self.notas = []
        self.edad: int
        self.asignaturas = []

    #Metodos

    def Saludar(self):
        print(f'Bievenido {self.nombre}')

    def AddNota(self, nota):
        if nota > 0 & nota < 10:
            self.nota.append(nota)
        else:
            print('Introduce una nota válida entre 0 y 10')

    def CumplirEdad(self):
       self.edad += 1

    def getNotas(self):
        print(self.notas)

    def addAsignatura(self, newAsig):
        self.asignaturas.append(newAsig)

    def delAsignatura(self, asign):
        self.asignaturas.remove(asign)

    def getAsig(self):
        for asign in self.asignaturas:
            print(asign)

    # Metodo t string (ya no me devuelve la posición, sino el contenido)
    def __str__(self):
        return f"['{self.nombre}']"

