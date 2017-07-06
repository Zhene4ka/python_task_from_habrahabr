from math import sqrt


#Составить программу нахождения корней квадратного уравнения в общем виде. Коэффициенты запрашиваются у пользователя.
a = int(input("Введите первый коэффициент квадратного уравнения:"))
b = int(input("Введите второй коэффициент квадратного уравнения:"))
c = int(input("Введите свободный член квадратного уравнения:"))
print("Квадратное уравнение имеет вид: {}x^2 + {}x + {} = 0".format(a,b,c))
d = b ** 2 - 4 * a * c
if d < 0:
    print("Нет решений")
else:
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    print(x1, x2)