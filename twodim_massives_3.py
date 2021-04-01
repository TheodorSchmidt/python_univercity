n = int(input())
m = int(input())
a = []
x = []
f = input().split()
for i in range(n):
    x.append(int(f[i]))
for i in range(n):
    a.append([])
    s = input().split()
    for j in range(m):
        a[i].append(s[j])
for i in range(n):
    for j in range(m):
        if j % 2 == 0:
            a[i][j] = x[i]
        a[i][j] = int(a[i][j])
for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()