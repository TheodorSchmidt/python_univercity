data = input().split()
n = int(data[0])
m = int(data[1])
d = dict({})
for i in range(n):
    a = input().replace(',', ' ').split()
    for j in range(len(a)):
        if j != 0:
            if d.get(a[0]) == None:
                d.update([(a[0], [a[j]])])
            else:
                d[a[0]].append(a[j])
res = list(d.items())
res.sort(key = lambda x: x[0])
res.sort(key = lambda x: len(x[1]), reverse = True)
for i in range(len(res)):
    print(res[i][0] + ' - ' + str(len(res[i][1])))