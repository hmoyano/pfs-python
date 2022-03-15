# Auth: Hector Moyano
# Exercise: 09
# data: 09/03/2022

def ex09():
    import math

    PI = math.pi
    R = int(input('Introduce el valor del radio del círculo:'))
    area = PI * math.pow(R, 2)

    print('El área de un círculo de radio', R, 'es:', area)