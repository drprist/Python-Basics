from sys import argv


def salary(a, b, c):
    sal = (a * b) + c
    return sal


script_name, productivity, rate, bonus = argv

print("Имя скрипта: ", script_name)
print("Выработка в часах: ", productivity)
print("Ставка в час: ", rate)
print("Премия: ", bonus)
print("Зарпалата: ", salary(int(productivity), int(rate), int(bonus)))
