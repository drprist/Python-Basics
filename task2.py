user_input = input("Введите несколько элементов через пробел : ")
list1 = user_input.split()
print("Введенный список: "'\n', list1)

i = 0
while i < len(list1):
    list1.insert((2 + i), list1.__getitem__(0 + i))
    list1.pop(0 + i)
    i = i + 2
print("Список с измененным порядком: "'\n', list1)
