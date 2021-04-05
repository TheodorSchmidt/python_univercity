def charIn(ch, st):
    st = st.lower()
    lst = list(st)
    new_st = []
    for i in range(len(lst)):
        if lst[i].isalpha():
            new_st.append(lst[i]) 
    k = 0
    for i in range(len(new_st)):
        if new_st[i] == ch[0]:
            k += 1
    if k == 0 or len(new_st) == 0:
        return 0
    else: 
        return float(k / len(new_st))
            

f_in = open('functions2_1_input.txt')
text = f_in.readlines()
f_in.close()
max = 0
ind = -1
max_str = ''
c = text[0]
for i in range(len(text)):
    if i != 0 and text[i] != '':
        percent = round(100 * charIn(c, text[i]))
        if percent > max:
            max = percent
            max_str = text[i]
            ind = i + 1 
f_out = open('functions2_1_output.txt', 'w')
f_out.write(str(max) + ' ' + str(ind))
f_out.close()
print(max_str)