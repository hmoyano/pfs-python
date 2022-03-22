# Auth: Hector Moyano
# Exercise: 18
# data: 14/03/2022

def ex18():

    from tkinter import messagebox

    first = int(input('Introduzca el primer número: '))
    second = int(input('Introduzca el segundo número: '))
    signo = str(input('Introduce el signo aritmético: '))

    if signo == '+':
        print('El resultado es', first + second)
        solution = str(first + second)
    elif signo == '-':
        print('El resultado es', first - second)
        solution = str(first - second)
    elif signo == '*':
        print('El resultado es', first * second)
        solution = str(first * second)
    elif signo == '/':
        print('El resultado es', first / second)
        solution = str(first / second)
    elif signo == '^':
        print('El resultado es', first ** second)
        solution = str(first ** second)
    elif signo == '%':
        print('El resultado es', first % second)
        solution = str(first % second)

    messagebox.showinfo(message="El resultado es " + solution, title="Mensaje de resultado")