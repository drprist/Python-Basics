def max_digit(a, b):
    d = b.index(a)
    c = int(b.index(a)) - 1
    if c < 0:
        c = 0
    if b[d] > b[c]:
        return a
    elif b[d] == b[c]:
        return 0
    else:
        return 0


my_list = [12, -40, 1, 2, 6, 5, 9, 45, 13, 14, 62]
new_list = [max_digit(el, my_list) for el in my_list if max_digit(el, my_list) != 0]
print(f"Исходный список:\n {my_list}")
print(f"Элементы исходного списка, значения которых больше предыдущего элемента:\n {new_list}")
