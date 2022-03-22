# Auth: Hector Moyano
# Exercise: 16
# data: 14/03/2022

def ex16():

    day = str(input('Introduce un día de la semana para comprobar si es laborable: '))

    if  day.upper() == 'SÁBADO' or day.upper() == 'DOMINGO':
        print('El', day,'es festivo.')
    elif    day.upper() == 'LUNES' or day.upper() == 'MARTES' or day.upper() == 'MIERCOLES':
        print('El', day, 'es laborable.')
    elif    day.upper() == 'JUEVES' or day.upper() == 'VIERNES':
        print('El', day, 'es laborable.')
    else:
            print("No has introducido un día de la semana válido, revisa la ortografía")

