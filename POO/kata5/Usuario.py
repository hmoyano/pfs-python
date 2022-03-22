# Autor: Hector
# version: 0.0.1
# data: 15/03/2022

class Usuario():
    # atributos de clase
    id: str
    nombre: str
    apellido: str
    email: str

    # atributos de instancia
    def __init__(self, NewNom, NewApe):
        self.id = '1234AV'
        self.nombre = NewNom
        self.apellido = NewApe
        self.email = "admin@gmail.com"

    # métodos propios
    def getName(self):
        print(f'Bienvenido {self.nombre}')