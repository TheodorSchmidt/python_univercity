s = input().split()
k = 0
for i in range(len(s)):
    s[i] = int(s[i])
    if s[i] % 2 != 0:
        k += 1
if k != 0:
    print(k)
else:
    print('Нет нечетных чисел')