s1 = input().split()
s2 = input().split()
a = []
b = []
set1 = set([])
set2 = set([])
for i in range(len(s1)):
    a.append(abs(int(s1[i])))
for i in range(len(s2)):
    b.append(abs(int(s2[i])))
for i in range(len(a)):
    while (a[i] // 10) > 0:
        set1.add(a[i] % 10)
        a[i] = a[i] // 10
    if a[i] != 0:
        set1.add(a[i])
for i in range(len(b)):
    while (b[i] / 10) > 0:
        set2.add(b[i] % 10)
        b[i] = b[i] // 10
    if b[i] != 0:
        set2.add(b[i])
l1 = list(set1.intersection(set2))
l2 = list(set1.union(set2))
l3 = list(set1.difference(set2))
l4 = list(set2.difference(set1))
l5 = list(set1.symmetric_difference(set2))
l1.sort()
l2.sort()
l3.sort()
l4.sort()
l5.sort()
print(l1)
print(l2)
print(l3)
print(l4)
print(l5)