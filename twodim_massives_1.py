n = int(input())
a = []
for i in range(n):
    a.append([])
    s = input()
    for j in range(n):
        a[i].append(s[j])
fl = False
ch = '-'
k = 0
for i in range(n):
    k = 0
    ch = '-'
    for j in range(n): 
        if a[i][j] != ch[0]: 
            k = 0
            if a[i][j] != '.':
                ch = a[i][j]
                k = 1
        else:
            k += 1
        if k == 3:
            fl = True
            res = ch[0]
if fl != True:
    for j in range(n):
        k = 0
        ch = '-'
        for i in range(n): 
            if a[i][j] != ch[0]:
                k = 0
                if a[i][j] != '.':
                    ch = a[i][j]
                    k = 1
            else:
                k += 1
            if k == 3:
                fl = True
                res = ch[0]
if fl == True:
    print(res)
else:
    print('-')