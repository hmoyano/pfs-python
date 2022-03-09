# Auth: Hector Moyano
# Exercise: 02
# data: 09/03/2022

def ex06():
    A = int(input('Introduce el valor de A:'))
    B = int(input('Introduce el valor de B:'))

    if A > B:
        print("A es mayor que B")
    elif B > A:
        print("B es mayor que A")
    if A == B:
        print("A y B son iguales")