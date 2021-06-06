dict_1 = dict()
with open('examples/text_6.txt', encoding='utf-8') as f:
    for line in f:
        name, rest = line.split(':')
        rest = rest.split()
        num = 0
        for part in rest:
            if "-" in part:
                continue
            nums, type1 = part.split('(')
            num += int(nums)
        dict_1[name] = num
print(dict_1)
