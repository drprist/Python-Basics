def split(x, y):
    z = x / y
    return z


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

try:
    print(f"Частное от деления {a} на {b} = {split(a, b)}")
except ZeroDivisionError:
    print('Деление на ноль')
