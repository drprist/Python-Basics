list_r = [12, 8, 6, 5, 4, 2]

new_r = int(input("Введите новый элемент рейтинга: "))
for i in list_r:
    if new_r > i:
        list_r.insert((list_r.index(i)), new_r)
        break
    elif new_r <= int(list_r[len(list_r) - 1]):
        list_r.append(new_r)
        break
print(list_r)
