#треугольник
class NotValidFigure(Exception):
    pass

from math import *

class Triangle:
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

        if not self.is_valid():
            raise NotValidFigure

    def perimetr(self): #перимитр 
        return round(self.a + self.b + self.c, 2)

    def plohad(self): #площадь 
        self.p = (self.a + self.b + self.c) // 2 
        return round(sqrt(self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c)), 2)

    def is_valid(self):
        sides = sorted([self.a, self.b, self.c ])
        # if (self.__c + self.__b) > self.__a and (self.__a + self.__b) > self.__c and (self.__c + self.__a) > self.__b:
        if all([isinstance(side, (float, int)) and side > 0 for side in sides]):
            return sides[2] < sides[0] + sides[1]

triangle = Triangle(5, 8, 3)
print(triangle.perimetr())
print(triangle.plohad())
print(triangle.is_valid())

# круг
class NotValidFigure(Exception):
    pass

from math import pi

class Сircle:
    
    def __init__(self, r):
        self.r = r

        if not self.is_valid():
            raise NotValidFigure

    def dlina_okr(self): #длина окружности
        return round(2 * pi * self.r, 2)
        
    def plohad(self): #площадь 
        return round(pi * self.r ** 2, 2)

    def is_valid(self):
        if isinstance(self.r, (float, int)):
            return self.r > 0

circle = Сircle(2.5)
print(circle.dlina_okr())
print(circle.plohad())
print(circle.is_valid()) 
