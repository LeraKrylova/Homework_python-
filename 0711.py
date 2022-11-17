# треугольник 
from math import *

class Triangle:
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


    def perimetr(self): #перимитр 
        return round(self.a + self.b + self.c)
        
    def plohad(self): #площадь 
        self.p = (self.a + self.b + self.c) / 2
        return round(sqrt(self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c)), 2)
        

triangle = Triangle(.1, .3, .2)
print(triangle.perimetr())
print(triangle.plohad())


#круг
class Сircle:
    
    def __init__(self, r):
        self.r = r

    def dlina_okr(self): #длина окружности
        return round(2 * pi * self.r)
        
    def plohad(self): #площадь 
        return round(pi * self.r ** 2, 2)

circle = Сircle(5)
print(circle.plohad())
print(circle.dlina_okr())
