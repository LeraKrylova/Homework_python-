from curses.ascii import isupper


str_ = input('Введите строку: ')
list_ = []
counter = 0
li = [] #[4]
list_ = str_.split(' ') #делит строку на части по конкретному знаку ['VJFJbvnnh', 'vhjfhvn', 'vhjgj']
for i in list_:
    for k in i:
        if k.isupper():
            counter += 1
    if counter >= 2:
        li.append(counter)
        counter = 0
result = (len(li) * 100 )/ len(list_) 
print(result, '%')
