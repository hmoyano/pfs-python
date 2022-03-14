# Auth: Hector Moyano
# Exercise: 17
# data: 14/03/2022

password = str('cocacola')

if str(input('Introduce la contraseña (1 de 3 intentos disponibles): ')) == password:
    print('Enhorabuena, contraseña correcta')
elif str(input('Introduce la contraseña (2 de 3 intentos disponibles): ')) == password:
    print('Enhorabuena, contraseña correcta')
elif str(input('Introduce la contraseña (3 de 3 intentos disponibles): ')) == password:
    print('Enhorabuena, contraseña correcta')
else:
    print("Error, 3 intentos fallidos.")


