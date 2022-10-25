from datetime import *

def diary_(list_, date):
    one_day = timedelta(days = 1)
    with open("diary.txt", "w") as f:
        for i in list_:
            f.write(str(date) + ':' + i + '\n')
            date = date + one_day

diary_(['привет', 'пока', 'снова привет', 'снова пока'], date(1789, 12, 20))
