n = int(input())
m = int(input())
a = []
for i in range(n):
    a.append([])
    s = input().split()
    for j in range(m):
        a[i].append(s[j])
for i in range(n):
    for j in range(m):
        a[i][j] = int(a[i][j])
min = 1000000
jmin = 0
max = -1000000
jmax = 0
for i in range(n):
    for j in range(m):
        if a[i][j] < min:
            min = a[i][j]
            jmin = j
        if a[i][j] >= max:
            max = a[i][j]
            jmax = j
amin = []
amax = []
for i in range(n):
    for j in range(m):
        if j == jmin:
            amin.append(a[i][j])
        if j == jmax:
            amax.append(a[i][j])
for j in range(m):
    if j == jmin:
        for i in range(n):
            a[i][j] = amax[i]
    if j == jmax:
        for i in range(n):
            a[i][j] = amin[i]
for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()