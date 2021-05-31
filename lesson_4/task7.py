import math


def fact(a):
    a = list(a)
    for i in list(a):
        b = math.factorial(i)
        yield b


n = int(input("Введите число: "))
n_1 = list(range(1, n + 1))
c = 0
for el in fact(n_1):
    print(str(n_1[c]) + "! = ", el)
    c += 1
