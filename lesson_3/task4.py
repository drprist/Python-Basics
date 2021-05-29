def degree(x, y):
    return x ** y


a = input("Введите действительное положительное число: ")
b = input("Введите целое отрицательное число: ")

print(a + " в степени " + b + ": " + str(degree(float(a), int(b))))
