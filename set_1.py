n = int(input())
a = set([])
s = ''
for i in range(n):
    s = input().split()
    for j in range(len(s)):
        a.add(s[j])
print(len(a))