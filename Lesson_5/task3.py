with open('examples/text_3.txt', 'r', encoding='utf-8') as f:
    names = []
    all_income = 0
    num = 0
    min_income = 20000
    for line in f:
        num += 1
        name, income = (i for i in line.split())
        income = float(income)
        if income < min_income:
            names.append(name)
        all_income += income
    all_income /= num
print(f'Сотрудники, имеющие оклад менее 20 тысяч:')
print(*names, sep=', ')
print('Средняя величина дохода сотрудников: ', all_income)
