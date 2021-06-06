lines = 0
words = 0
letters = 0

for line in open('examples/text_2.txt', 'r'):
    lines += 1
    letters += len(line)
    pos = 'out'
    for letter in line:
        if letter != ' ' and pos == 'out':
            words += 1
            pos = 'in'
        elif letter == ' ':
            pos = 'out'
    print("Строка №", lines, "Количество слов: ", words)
    words = 0
print("Строк всего:", lines)
