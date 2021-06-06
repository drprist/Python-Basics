with open("examples/text_1.txt", "w", encoding='utf-8') as f:
    while True:
        text = input("Введите данные для записи: ")
        if not text:
            break
        f.write(text + '\n')
