import random
import string

cif = string.digits
alf_u = string.ascii_uppercase
alf_l = string.ascii_lowercase
sp = '!«»#$%&()*+:;=?@~'
password = random.choice(alf_u) + random.choice(alf_l) + random.choice(cif) \
          + random.choice(cif) + random.choice(sp) + random.choice(sp)
symb = list(cif + alf_l + alf_u)
random.shuffle(symb)
for _ in range(6):
    password += random.choice(symb)
password = list(password)
random.shuffle(password)
print(''.join(password))