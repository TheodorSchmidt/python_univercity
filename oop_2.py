from math import sqrt

class Vector:
    def __init__(self, *args):
        '''Создание класса'''
        self.components = list(args)
    def dim(self):
        '''Размерность вектора'''
        return len(self.components)
    def __eq__(self, other):
        '''Проверка на равенство векторов'''
        if self.dim() == other.dim():
            for i in range(len(self.components)):
                if self.components[i] != other.components[i]:
                    return False
            return True
        else:
            return('Вектора разной размерности')
    def __ne__(self, other):
        '''Проверка на неравенство векторов'''
        if self.dim() == other.dim():
            for i in range(len(self.components)):
                if self.components[i] != other.components[i]:
                    return True
            return False
        else:
            return('Вектора разной размерности')
    def __add__(self, other):
        '''Сложение двух векторов'''
        new_comp = []
        if self.dim() == other.dim():
            for i in range(len(self.components)):
                new_comp.append(self.components[i] + other.components[i])
            return Vector(*new_comp)
        else:
            return('Вектора разной размерности')
    def __mul__(self, other): 
        '''Скалярное произведение и произведение вектора на число'''
        if type(other) == int or type(other) == float:
            new_comp = []
            for i in range(len(self.components)):
                new_comp.append(self.components[i] * other)
            return Vector(*new_comp)
        else:
            prod = 0
            if self.dim() == other.dim():
                for i in range(len(self.components)):
                    prod += self.components[i] * other.components[i]
                return prod
            else:
                return('Вектора разной размерности') 
    def __getitem__(self, item):
        '''Получение элемента по индексу'''
        try:
            return self.components[item]
        except:
            return('Выход за границы размерности вектора')
    def __setitem__(self, item, val):
        '''Изменение элемента по индексу'''
        try:
            self.components[item] = val
        except:
            print('Выход за границы размерности вектора')
    def __str__(self):
        '''Перевод класса в строку'''
        return str(self.components)
    def __abs__(self):
        '''Модуль вектора'''
        sum = 0
        for i in range(len(self.components)):
            sum += self.components[i] * self.components[i]
        return sqrt(sum)
    def isCollin(self, other):
        '''Проверка на коллинеарность векторов'''
        if self.dim() == other.dim():
           if self.components.count(0) == len(self.components) \
           or other.components.count(0) == len(other.components):
               return('Один из векторов или оба являются нулевыми')
           else:
               rel = 0
               for i in range(len(self.components)):
                   if self.components[i] == 0 and other.components[i] == 0:
                       continue
                   elif self.components[i] == 0 or other.components[i] == 0:
                       return(False)
                   else:
                       if rel == 0:
                           rel = self.components[i] / other.components[i]
                       else:
                           if (self.components[i] / other.components[i]) != rel:
                               return(False)
               return(True)

        else:
            return('Вектора разной размерности')
    def norm(self):
        modul = abs(self)
        new_comp = []
        for i in range(len(self.components)):
            new_comp.append(self.components[i] / modul)
        return Vector(*new_comp)

v = Vector(2, 3, 4, 5)
v1 = Vector(2, 3, 4, 5)
v2 = Vector(2, 3, 4, 5)
v3 = Vector(2, 4, 3, 2)
v4 = Vector(1, 2, 3)
v5 = Vector(4, 6, 0, 10)
v6 = Vector(4, 6, 8, 10)
v7 = Vector(0, 0, 0, 0)
v8 = Vector(4, 8, 8, 10)
print("ПРОВЕРКА НА РАВЕНСТВО")
print(v1, v2, v1.__eq__(v2))
print(v1, v3, v1.__eq__(v3))
print(v1, v4, v1.__eq__(v4))
print('')
print("ПРОВЕРКА НА НЕРАВЕНСТВО")
print(v1, v2, v1.__ne__(v2))
print(v1, v3, v1.__ne__(v3))
print(v1, v4, v1.__ne__(v4))
print('')
print("СЛОЖЕНИЕ ВЕКТОРОВ")
print(v1, v3, v1.__add__(v3))
print(v3, v4, v3.__add__(v4))
print('')
print("СКАЛЯРНОЕ УМНОЖЕНИЕ ВЕКТОРОВ")
print(v1, v3, v2.__mul__(v3))
print('')
print("УМНОЖЕНИЕ ВЕКТОРА НА ЧИСЛО")
print(v4, 10, v4.__mul__(10)) 
print('')
print("ВЗЯТИЕ ПО ИНДЕКСУ")
print(v1, 'v1[2]: ', v1[2]) 
v1[2] = 7
print('v1[2] = 7 ', v1)
print(v1, 'v1[10]: ', v1[10])
print('')
print("МОДУЛЬ ВЕКТОРА")
print(v3, abs(v3))
print(v4, abs(v4))
print('')
print("КОЛЛИНЕАРНОСТЬ ВЕКТОРОВ")
print(v, v2, v.isCollin(v2))
print(v, v5, v.isCollin(v5))
print(v, v6, v.isCollin(v6))
print(v, v7, v.isCollin(v7))
print(v, v8, v.isCollin(v8))
print('')
print("НОРМИРОВАННЫЙ ВЕКТОР")
print(v, v.norm())
print(v8, v8.norm())
print(v4, v4.norm())