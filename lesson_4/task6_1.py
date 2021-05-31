from itertools import count
from sys import argv


def gen(a):
    for el in count(a):
        if el > 15:
            break
        else:
            print(el)


script_name, digit = argv

print("Имя скрипта: ", script_name)
print("Начальное число: ", digit, "\nСгенерированные целые числа, начиная с указанного: ")
gen(int(digit))
