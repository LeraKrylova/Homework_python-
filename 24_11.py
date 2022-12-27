class NotValidFigure(Exception):
    pass

import csv 

class Building:
    def __init__(self, floors: int, height: int, width: int, name: str):
        self.floors = floors #этажи
        self.height = height #высота
        self.width = width #ширина
        self.name = name #название 
        if not self.is_valid():
            raise NotValidFigure('Коректно введите данные')

    def is_valid(self):
        buil_ = self.floors, self.height, self.width 
        return all([float(bui) > 0 for bui in buil_])

    @classmethod
    def from_tuple(cls, data):
        return cls(*data)

    def __str__(self):
        return 'этажи : {0}, высота : {1}, ширина : {2}, название : {3}'.format(self.floors, self.height, self.width, self.name)

    def to_tuple(self):
        return self.floors, self.height, self.width, self.name


def bul(building):
    with open('domic', 'a') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(building.to_tuple())
    print('Данные о здание {}, успешно добавлены в файл'.format(n_))

def read():
    with open('domic', 'rt') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(Building.from_tuple(row))
    # return csv_reader

        # return csv_reader
        # building_csv = [Building.from_tuple(row) for row in csv_reader]

f = 'Введите количество этажей:'
h = 'Введите высоту здания:'
w = 'Введите ширину здания:'
n = 'Введите название здания:'



print('Вы будете записывать данные о здании или читать? 0/1')
d  = input()
if d == '0':
    try:
        f_, h_, w_, n_ =  int(input(f, )), int(
            input(h )), int(input(w, )), input(n, )
    except TypeError:
        print('Неправильно ввели данные, попробуйте еще раз!')
    building = Building(f_, h_, w_, n_)
    bul(building)
elif d == '1':
    read()
