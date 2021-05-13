import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas

#1
t = np.linspace(0, 2*np.pi, 100)
x = np.sin(t)
plt.figure()
plt.plot(x)
plt.title("Sin")
plt.axis([0, 100, -1, 1])
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.show()
plt.savefig('matplotlib_task1.png')

#2
matr = np.random.randint(0, 10000, (10, 1000))
sum_mas = matr.sum(axis=0)
plt.figure() 
plt.hist(sum_mas, cumulative=True)
plt.show()
plt.savefig('matplotlib_task2.png')

#3 
tips = sns.load_dataset('tips')
tips.head()
cols = tips.columns.tolist()
print("Названия колонок:", cols)
types = tips.dtypes
names = []
for i in types:
    names.append(i.name)
print("Типы данных: ", names)
size = tips.size
print("Размер: ", size)
last_five = tips[-5:]
print("Последние пять элементов:\n", last_five) 

#4
meancost = tips.groupby(['smoker', 'day', 'time'])['total_bill'].mean()
print("Средняя стоимость в чеке:\n", meancost)

#5
meancost.hist()
plt.show()
plt.savefig('matplotlib_task5.png')

#6
illnes = pandas.read_csv('table2.csv')
print(illnes)
print(illnes.rate.str.split("/", expand=True))

#7
illnes[['cases', 'population']] = illnes.rate.str.split("/", expand=True)
illnes = illnes.drop(['rate'], axis=1)
print(illnes)