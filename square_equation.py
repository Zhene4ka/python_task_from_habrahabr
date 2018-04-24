import math

a = int(input("Введите старший коэффициент квадратного уравнения:\n"))
b = int(input("Введите b:\n"))
c = int(input("Введите c:\n"))

print("a ={}, b = {}, c = {}".format(a, b, c))

d = b ** 2 - 4 * a * c

if d < 0:
    print("Нет решений")
else:
    x_1 = int((- b + d ** (1/2)) / (2 * a))
    x_2 = int((- b - d ** (1/2)) / (2 * a))
    print(x_1, x_2)
