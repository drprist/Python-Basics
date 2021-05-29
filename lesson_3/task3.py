def max_sum(a, b, c):
    d = [a, b, c]
    x = sorted(d)[1] + sorted(d)[2]
    return x


user_a = int(input("Введите первое число: "))
user_b = int(input("Введите второе число: "))
user_c = int(input("Введите третье число: "))

print("Сумма двух наибольших аргументов: " + str(max_sum(user_a, user_b, user_c)))
