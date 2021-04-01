s = input().split()
res = []
for i in range(len(s)):
    if len(s[i]) > 5:
        res.append(s[i])
for i in range(len(res)):
    print(res[i])