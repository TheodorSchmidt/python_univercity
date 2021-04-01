import datetime
import calendar

def week(data):
    '''Возвращает название дня недели из даты.

    На вход принимается аргумент в формате date'''
    return ' - ' + calendar.day_name[data.weekday()]

enter = input().split('.')
n = int(input())
for i in range(3): enter[i] = int(enter[i])
dat = datetime.date(enter[2], enter[1], enter[0])
dat1 = dat + datetime.timedelta(days = n)
dat2 = dat - datetime.timedelta(days = n)
print(dat1.strftime('%d.%m.%Y'), end = '')
print(week(dat1))
print(dat2.strftime('%d.%m.%Y'), end = '')
print(week(dat2))