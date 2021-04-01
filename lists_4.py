s = input().split(',')
res = []
for i in range(len(s)):
    f = s[i].replace('_', 'k')
    if f.isalnum() == False:
        res.append(s[i])
res.sort()
max = 0
for i in range(len(res)):
    if len(res[i]) > max:
        max = len(res[i]) 
for i in range(len(res)):
    print(res[i].rjust(max,' '))