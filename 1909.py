def data(day: int, month: int, year: int):
    month_31_d = [1, 3, 5, 7, 8, 10, 12]
    month_30_d = [4, 6, 9, 11]
    if 0 < day <= 31 and month in month_31_d:
        return True
    if 0 < day <= 30 and month in month_30_d:
        return True
    if month == 2:
        if year % 100 != 0 and year % 4 == 0 or year % 400 == 0:
            if 0 < day <= 29:
                return True
        if 0 < day <= 28:
            return True
    return False
    
print(data(22, 5, 2020))
