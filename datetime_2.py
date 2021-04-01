import datetime
import calendar

def week(data):
    '''Возвращает название дня недели из даты.

    На вход принимается аргумент в формате date'''
    return '- ' + calendar.day_name[data.weekday()]

enter = input().split('.')
for i in range(3): enter[i] = int(enter[i])
dat = datetime.date(enter[2], enter[1], enter[0])
cur_dat = datetime.date.today()
days = cur_dat - dat
d = abs(days.days)
if days.days < 0:
    print('Дата на ' + str(d) + ' дней позже')
else:
    print('Дата на ' + str(d) + ' дней раньше')
print(dat.strftime('%d.%m.%Y'), week(dat))
print()