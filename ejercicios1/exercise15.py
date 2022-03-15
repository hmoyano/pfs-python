# Auth: Hector Moyano
# Exercise: 15
# data: 14/03/2022

def ex15():

    nventas = int(input("Introduce el número total de ventas: "))
    sumventas = 0
    a = 1

    while a <= nventas:
        venta = float(input("Venta nº" + str(a) + ": "))
        sumventas = float(sumventas) + float(venta)
        a += 1

    if nventas == 1:
        print("El importe total de la venta es: ", sumventas)
    elif nventas == 0:
        print("El número total de ventas es 0 y por lo tanto su importe también es 0.")
    else:
        print("El importe total de las", nventas, "ventas es: ", sumventas)

