# Auth: Hector Moyano
# Exercise: 02
# data: 02/03/2022

#variables de entorno

X = int(8)
Y = int(7)

N = float(5.45)
M = float(3.25)

# procesado de datos

SumaInt = X + Y
DifInt = X - Y
MultInt = X * Y
DivInt = X / Y
RestInt = X % Y

SumaFloat = N + M
DifFloat = N - M
MultFloat = N * M
DivFloat = N / M
RestFloat = N % M

SumaXN = X + N
DivYM = Y / M
RestYM = Y % M

DoubleX = 2 * X
DoubleY = 2 * Y
DoubleN = 2 * N
DoubleM = 2 * M

SumaTotal = X + Y + N + M
MultTotal = X * Y * N * M


# output de datos

print("Valor de X", X)
print("Valor de Y", Y)
print("Valor de N", N)
print("Valor de M", M)

print("Suma de X e Y", SumaInt)
print("Diferencia de X e Y", DifInt)
print("Producto de X e Y", MultInt)
print("Cociente de X e Y", DivInt)
print("Resto de X e Y", RestInt)

print("Suma de N y M", SumaFloat)
print("Diferencia de N y M", DifFloat)
print("Producto de N y M", MultFloat)
print("Cociente de N y M", DivFloat)
print("Resto de N y M", RestFloat)

print("Suma de X y N", SumaXN)
print("Cociente de Y y M", DivYM)
print("Resto de Y y M", RestYM)

print("Doble de X", DoubleX)
print("Doble de Y", DoubleY)
print("Doble de N", DoubleN)
print("Doble de M", DoubleM)

print("Suma de todas las variables", SumaTotal)
print("Producto de todas las variables", MultTotal)