num_1 = int(input('Введите целое положительное число: '))
i = 0
p = num_1

while p // 10 or p % 10:
    n = p % 10
    if n > i:
        i = n
        p = p // 10
    else:
        p = p // 10
print("Наибольшая цифра числа ", num_1, "-", i)
