import itertools

n = input().split()
s = set()
for i in range(len(n)):
    s.add(n[i])
s = list(s)
res = []
for j in itertools.count():
    if j > len(s): break
    for i in itertools.combinations(s, j):
        for k in itertools.permutations(i):
            lst = list(k)
            sr = ''.join(lst)
            if sr != '':
                if len(sr) == 1 or sr[0] != '0':
                    res.append(sr)

for i in range(len(res)):
    res[i] = int(res[i])
res.sort()
print(len(res))
print(res)