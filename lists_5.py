res = []
for i in input().split():
    if i.isdigit():
        res.append(int(i))
    else:
        if i == '+':
            a = res[-2]
            b = res[-1]
            res.pop()
            res.pop()
            res.append(a + b)
        if i == '-':
            a = res[-2]
            b = res[-1]
            res.pop()
            res.pop()
            res.append(int(a - b))
        if i == '*':
            a = res[-2]
            b = res[-1]
            res.pop()
            res.pop()
            res.append(int(a * b))
        if i == '/':
            a = res[-2]
            b = res[-1]
            res.pop()
            res.pop()
            res.append(int(a / b))
        if i == '~':
            a = res[-1]
            res.pop()
            res.append(int(0 - a))
        if i == '!':
            a = res[-1]
            res.pop()
            sum = 1
            for k in range(1, a + 1):
                sum *= k
            res.append(sum)
        if i == '#':
            a = res[-1]
            res.pop()
            res.append(a)
            res.append(a)
        if i == '@':
            a = res[-3]
            b = res[-2]
            c = res[-1]
            res.pop()
            res.pop()
            res.pop()
            res.append(b)
            res.append(c)
            res.append(a)
print(res[0])