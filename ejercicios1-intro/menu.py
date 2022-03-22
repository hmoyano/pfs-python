# Auth: Hector Moyano
# Menu
# data: 14/03/2022

from ejercicios1 import exercise01

def menu():
    ejercicio = 0
    while (ejercicio < 1 or ejercicio > 18):
        ejercicio = int(input("Qué ejercicio desea ejecutar (1 - 18): "))

    if ejercicio == 1:
        ej1()
    if ejercicio == 2:
        ej2()
    if ejercicio == 3:
        ej3()
    if ejercicio == 4:
        ej4()
    if ejercicio == 5:
        ej5()
    if ejercicio == 6:
        ej6()
    if ejercicio == 7:
        ej7()
    if ejercicio == 8:
        ej8()
    if ejercicio == 9:
        ej9()
    if ejercicio == 10:
        ej10()
    if ejercicio == 11:
        ej11()
    if ejercicio == 12:
        ej12()
    if ejercicio == 13:
        ej13()
    if ejercicio == 14:
        ej14()
    if ejercicio == 15:
        ej15()
    if ejercicio == 16:
        ej16()
    if ejercicio == 17:
        ej17()
    if ejercicio == 18:
        ej18()
    print("El ejercicio %i ha finalizado", ejercicio)