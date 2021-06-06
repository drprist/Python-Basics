dict_1 = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('examples/text_4.txt', 'r', encoding='utf-8') as f:
    with open('examples/text_4_1.txt', 'w', encoding='utf-8') as f2:
        for line in f:
            en, *num = line.split()
            ru = dict_1[en]
            f2.write(' '.join([ru] + num) + '\n')
