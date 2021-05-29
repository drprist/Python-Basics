import sys


def upper_first_letter(a):
    list_1 = list(a)
    for d in list_1:
        if 97 <= ord(d) <= 122:
            continue
        else:
            print("Ошибка ввода. Требовалось ввести слова из латинских букв нижнего регисра.")
            sys.exit()
    a2 = list_1[0]
    a2 = a2.upper()
    list_1.pop(0)
    list_1.insert(0, a2)
    str_1 = ''.join(list_1)
    return str_1


user_type = input("Введите строку из слов из маленьких латинских букв: ")
str_2 = user_type.split()
list_clear = list()
for i in str_2:
    i = upper_first_letter(i)
    list_clear.append(i)
print(f"Введенная строка, слова с заглавной буквы: ", ' '.join(list_clear))
