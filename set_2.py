s = input().split()
a = []
b = []
set1 = set([])
set2 = set([])
for i in range(len(s)):
    if len(s[i]) == 2:
        a.append(int(s[i]))
    else:
        b.append(int(s[i]))
for i in range(len(a)):
    while (a[i] // 10) > 0:
        set1.add(a[i] % 10)
        a[i] = a[i] // 10
    set1.add(a[i])
for i in range(len(b)):
    while (b[i] / 10) > 0:
        set2.add(b[i] % 10)
        b[i] = b[i] // 10
    set2.add(b[i])
l = list(set1.difference(set2))
l.sort()
print(l)