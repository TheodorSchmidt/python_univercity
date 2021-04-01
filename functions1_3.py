n = input().split()
ans = list(filter(lambda x: len(x) == 2, n))
for i in range(len(ans)):
    ans[i] = int(ans[i])
print(ans)