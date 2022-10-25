str_ = input('Ведите строку: ')
stroki = str_.split(' ')


result = 0
for i in stroki:
    k = 0
    for s in i:
        if s.isupper():
            k += 1
    if k > len(i) / 2:
        result += 1


p = (result / len(stroki)) * 100

print(p, '%')
