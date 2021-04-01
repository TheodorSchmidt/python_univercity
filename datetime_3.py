import datetime
import calendar

def week(data):
    '''Возвращает название дня недели из даты.

    На вход принимается аргумент в формате date'''
    return '- ' + calendar.day_name[data.weekday()]

def isLeap(year):
    '''Возвращает истину, если год високосный.
    
    На вход принимается год в формате int'''
    if (year % 4 != 0) or (year % 100 == 0) and (year % 400 != 0):
        return False
    else:
        return True

def printNextBirth(age, year, month, day):
    '''Распечатывает выходные данные

    На вход принимается возраст, год, месяц, день в формате int'''
    print("Возраст " + str(age) + " лет")
    if month == 2 and day == 29 and isLeap(year) == False:
        month = 3
        day = 1
    next_birth = datetime.date(year, month, day)
    print(next_birth.strftime('%d.%m.%Y'), week(next_birth))

enter = input().split('.')
for i in range(3): enter[i] = int(enter[i])
birth = datetime.date(enter[2], enter[1], enter[0])
cur_data = datetime.date.today()
age = cur_data.year - birth.year

if cur_data.month < birth.month:
    fl = False
elif cur_data.month > birth.month:
    fl = True
else:
    if cur_data.day < birth.day:
        fl = False
    else:
        fl = True
if fl == False:
    printNextBirth(age - 1, cur_data.year, birth.month, birth.day)
else:
    printNextBirth(age, cur_data.year + 1, birth.month, birth.day)