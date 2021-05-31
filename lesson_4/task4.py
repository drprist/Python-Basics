def copy(a, b):
    x = [i for i, ltr in enumerate(a) if ltr == b]
    return len(x)


my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [el for el in my_list if copy(my_list, el) == 1]

print(f"Представленный список чисел: \n", my_list)
print(f"Элементы списка, не имеющие повторений: \n", new_list)
