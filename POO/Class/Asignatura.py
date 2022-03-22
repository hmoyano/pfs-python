
class Asignatura():

    # Atributos de clase

    nombre: str
    nota: int

    # Constructor

    def __init__(self, newNombre):
        self.nombre = newNombre
        self.nota: int

    # Metodos

    def addNota(self, newNota):
        if 0 <= newNota <= 10:
            self.nota = newNota
        else:
            print('Introduce nota válida')


    # Metodo t string (ya no me devuelve la posición, sino el contenido)
    def __str__(self):
        return f"['{self.nombre}',{self.nota}]"

