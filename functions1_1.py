def DecToBin(x):
    '''Переводит число из десятичной СС в двоичную.

    Значение должно быть целым числом.'''
    x = int(x)
    res = ''
    while x > 0:
        res = str(x % 2) + res
        x = x // 2
    return int(res)

n = input().split()
ans = []
for i in range(len(n)):
    ans.append(DecToBin(n[i]))
print(ans)