n = int(input())
d = dict()
for i in range(n):
    s = input()
    date = s[:(s.find(' '))]
    s = s[(s.find(' ')) + 1:]
    time = s[:(s.find(' '))]
    time = time.split('.')
    ntime = ''
    for i in range(len(time)):
        time[i] = int(time[i])
        if time[i] < 10:
            ntime += '0' + str(time[i])
        else:
            ntime += str(time[i])
    task = s[(s.find(' ')) + 1:]
    date = date.split('.')
    ndate = ''
    for i in range(len(date)):
        date[i] = int(date[i])
        if date[i] < 10:
            ndate += '0' + str(date[i]) + '.'
        elif i == 2:
            ndate += str(date[i])
        else:
            ndate += str(date[i]) + '.'
    if d.get(ndate) == None:
        d.update([(ndate, [(ntime, task)])])
    else:
        d[ndate].append((ntime, task))
    d[ndate].sort(key = lambda x: int(x[0]))
m = int(input())
dates = []
for i in range(m):
    date = input().split('.')
    ndate = ''
    for j in range(len(date)):
        date[j] = int(date[j])
        if date[j] < 10:
            ndate += '0' + str(date[j]) + '.'
        elif j == 2:
            ndate += str(date[j])
        else:
            ndate += str(date[j]) + '.'
    dates.append(ndate)
print('\n')
for i in range(m):
    print(dates[i])
    a = d.get(dates[i], [])
    for j in range(len(a)):
        time = a[j][0]
        task = a[j][1]
        print(time[:2] + '.' + time[2:] + ' ' + task)
    print('')