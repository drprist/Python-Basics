revenue = input("Введите значение выручки фирмы: ")
costs = input("Введите значение издержек фирмы: ")
profit = int(revenue) - int(costs)
prof_ability = int(revenue) / int(costs)

if profit > 0:
    print("Фирма отработала с прибылью!")
    print("Рентабильность фирмы составляет: ", round(prof_ability), "%")
    personal = input("Введите количество сотрудников фирмы: ")
    print("Прибыль фирмы на одного сотрудника составила: ", round(profit/int(personal)))
else:
    print("Фирма отработала с убытками!")
