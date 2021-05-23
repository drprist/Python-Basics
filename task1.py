list_1 = [12, 46.54, False, 'str', None, [2, 3], 6j, (7, 8), {12, -1}, {'first': 'second'}, b'text', 12]

i = 0
while i < len(list_1):
    t = str(type(list_1[i]))
    print(list_1[i], "это класс", t[8:(len(t)-2)])
    i += 1
