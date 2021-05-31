from itertools import cycle
from sys import argv


def gen(a):
    i = 0
    for el in cycle(a):
        if i > 20:
            break
        print(el)
        i += 1


script_name = argv

list_1 = [3, 4, 5, 6]
print("Имя скрипта: ", script_name)
print("Заранее определенный список: ", list_1, "\nПовторяющиеся элементы списка: ")
gen(list_1)
