words = input("Введите несколько слов, разделённых пробелами: ")
list_1 = words.split()

for i, list_1 in enumerate(list_1):
    if len(list_1) <= 10:
        print(i + 1, list_1)
    else:
        print(i + 1, list_1[0:10])
