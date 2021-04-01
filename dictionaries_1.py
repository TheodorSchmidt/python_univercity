mon = {'янв': [], 'фев': [], 'мар': [], 'апр': [], 'май': [], 'июн': [],
       'июл': [], 'авг': [], 'сен': [], 'окт': [], 'ноя': [], 'дек': []}
col = int(input())
for i in range(col):
    a = input().split()
    n = a[0]
    d = a[1]
    m = a[2]
    mon[m].append((n, d))
    mon[m].sort(key=lambda x: (x[1], x[0])) 
res = []
que = int(input())
for j in range(que):
    inputm = input()
    res.append(mon[inputm])
print(res)
for i in range(len(res)):
    if not res[i]:
        print('')
    else:
        q = res[i]
        string = ''
        for j in range(len(q)):
            string += q[j][0] + ' ' + str(q[j][1] + ' ')
        print(string)