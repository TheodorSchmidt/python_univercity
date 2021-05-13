import numpy as np
#1
data = np.loadtxt('wind-data-1977.csv', dtype=int, delimiter=',', comments='%', 
                  usecols=(0, 1, 2))
val = np.loadtxt('wind-data-1977.csv', dtype=float, delimiter=',', comments='%',
                  usecols=(3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))

#2
for i in data:
    if i[0] == 0:
        i[0] = 77

val = val.T 
for i in val:
    mask = np.isnan(i)
    mean_val = round(np.nanmean(i), 4)
    for j in range(len(mask)):
        if mask[j]:
            i[j] = mean_val
val = val.T

#3
print("#3 ВЫЧИСЛЕНИЕ ЗА ВСЕ ДНИ")
min_val = val.min()
print("Минимальное значение скорости ветра: \n", min_val)
max_val = val.max()
print("Максимальное значение скорости ветра: \n", max_val)
mean_val = val.mean()
print("Среднее значение скорости ветра: \n", mean_val)
std_val = val.std()
print("Среднее квадратическое значение скорости ветра: \n", std_val)

#4
print("#4 ДЛЯ КАЖДОЙ РЕПЕРНОЙ ТОЧКИ ПО ВСЕМ ДНЯМ")
min_rep = val.min(axis=0) 
print("Минимальное значение скорости ветра: \n", min_rep)
max_rep = val.max(axis=0)
print("Максимальное значение скорости ветра: \n", max_rep)
mean_rep = val.mean(axis=0)
print("Среднее значение скорости ветра: \n", mean_rep)
std_rep = val.std(axis=0)
print("Среднее квадратическое значение скорости ветра: \n", std_rep)

#5 
print("#5 ДЛЯ ВСЕХ РЕПЕРНЫХ ТОЧЕК ДЛЯ КАЖДОГО ДНЯ")
min_day = val.min(axis=1) 
print("Минимальное значение скорости ветра: \n", min_day)
max_day = val.max(axis=1)
print("Максимальное значение скорости ветра: \n", max_day)
mean_day = val.mean(axis=1)
print("Среднее значение скорости ветра: \n", mean_day)
std_day = val.std(axis=1)
print("Среднее квадратическое значение скорости ветра: \n", std_day)

max_day = np.reshape(max_day, (365, 1))
res = np.hstack((val, max_day))

#6
print("#6 ДЛЯ КАЖДОГО ДНЯ ТОЧКА С НАИБОЛЬШИМ ЗНАЧЕНИЕМ СКОРОСТИ ВЕТРА")
max_day_mas = val.argmax(axis=1)
print("Наибольшее значение скорости ветра: \n", max_day_mas)

#7
print("#7 ГОД, МЕСЯЦ И ДЕНЬ, КОГДА БЫЛА ЗАФИКСИРОВАНА САМАЯ БОЛЬШАЯ СКОРОСТЬ ВЕТРА") 
res_data = (val.argmax() + 1) // 12 - 1
print("Самая большая скорость ветра: \n", data[res_data])

#8
print("#8 СРЕДНЯЯ СКОРОСТЬ В ЯНВАРЕ ДЛЯ КАЖДОЙ РЕПЕРНОЙ ТОЧКИ")
jan_val = val[:31, :]
jan_mean = jan_val.mean(axis=0)
print("Средняя скорость: \n", jan_mean)

#9
output = np.concatenate((data, res), axis=1)

np.savetxt('numpy_lib_output.csv', output, delimiter=",", fmt='%2.0d,%1.0d,%1.0d,%2.4f,%2.4f,%2.4f,%2.4f,%2.4f,%2.4f,%2.4f,'
                                                              '%2.4f,%2.4f,%2.4f,%2.4f,%2.4f,%2.4f')
#10
days = np.array([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])
begin = 0
mean_val = []
for count in days:
    cur = val[begin:begin + count, :]
    mean_val.append(round(cur.mean(), 4)) 
    begin += count
print("Cредняя скорость ветра для каждого месяца:\n", mean_val)