with open('examples/text_5.txt', 'w', encoding='utf-8') as f:
    f.write(f"{' '.join([str(i) for i in range(1, 31)])}")
with open('examples/text_5.txt', 'r', encoding='utf-8') as f:
    numbers = [int(i) for i in f.read().split()]
    print("Сумма чисел в файле:", sum(numbers))
