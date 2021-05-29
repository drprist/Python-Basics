def all_sum(user_list):
    list_1 = user_list.split()
    a = 0
    for i in list_1:
        if i.lstrip('-').isdigit():
            a = a + int(i)
        else:
            return a, False
    return a, True


user_answer = 'y'
max_sum = 0
while user_answer == 'y':
    list_2 = input("Введите строку чисел, разделенных пробелом: ")
    x = all_sum(list_2)[0]
    max_sum = max_sum + x
    if all_sum(list_2)[1]:
        while user_answer != 'n':
            user_answer = str(input("Сумма всех введенных чисел равна: " + str(max_sum) + ". Продолжить ввод? (y / n)"))
            if user_answer == ('y' or 'n'):
                break
            else:
                print("Ошибка ввода. Попробуйте еще раз.")
    else:
        print("Сумма всех введенных чисел равна: " + str(max_sum))
        user_answer = 'n'
