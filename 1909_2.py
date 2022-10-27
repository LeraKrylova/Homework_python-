def date(day:int, month:int, year:int):
    m_31 = [1, 3, 5, 7, 8, 10, 12]
    m_30 = [4, 6, 9, 11]
    if month > 0 and day > 0 and month < 13 and day < 32:
        if day <= 31 and month in m_31:
            return True
        elif day <= 30 and month in m_30:
            return True
        elif month == 2:
            if ((year % 4 == 0 and (not year % 100 == 0) or year % 400 == 0) and day<=29) or (day <=28):
                return True
    return False 

print(date(31, 12, 2020))
