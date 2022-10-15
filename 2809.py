from datetime import date
from datetime import timedelta

def f(records, date):
    one_day = timedelta(days=1)
    f = open("diary.txt", "w")
    for record in records:
        f.write(str(date) + ': ' + record + '\n')
        date = date + one_day
    f.close()

f(['aaa', 'bbbb', 'ccc', 'dddd'],  date(1988, 1, 30))