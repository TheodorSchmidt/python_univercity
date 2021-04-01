s = input().split()
def isPositive(x):
    if x > 0:
        return True
    else:
        return False
for i in range(len(s)):
    s[i] = int(s[i])
res = filter(isPositive, s)
print(*res)