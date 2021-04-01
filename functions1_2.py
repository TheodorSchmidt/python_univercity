def permutations(n, m):
    '''Подсчет числа перестановок из m по n

    1 <= n <= m.'''
    if n == 1:
        return m
    else:
        return (m - n + 1) * permutations(n - 1, m)
n = int(input())
m = int(input())
ans = permutations(n, m)
print(ans)