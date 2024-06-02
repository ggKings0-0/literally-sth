import os
import time
from random import *
lbig = list('QWERTYUIOPASDFGHJKLZXCVBNM')
lsmall = list('qwertyuiopasdfghjklxcvbnm')
digits = list('0123456789')
spec = list('!?№@*&+-=')
symbols = lbig + lsmall + digits + spec
database = []
while len(database) < 20:
    len_pass = randint(8, 12)
    password = [choice(symbols) for _ in range(len_pass)]
    cbig, cdigit, cspec = 0, 0, 0
    for i in range(len_pass):
        if password[i] in lbig:
            cbig += 1
        elif password[i] in digits:
            cdigit += 1
        elif password[i] in spec:
            cspec += 1
    if cbig >= 2 and cdigit >= 2 and cspec >= 1:
        database.append(''.join(password))
users = [f'Users{i}' for i in range (1, 21)]
codes = [randint(100, 999) for i in range(20)]
us_pass = {d: u for u, d in zip(database, users)}
print(us_pass)
us_code = {c: u for u, c in zip(codes, users)}
print(us_code)
while True:
    username = input()
    if username in us_pass:
        pswrd = input()
        if pswrd == us_pass.get(username):
            clear = lambda: os.system('cls')
            print(us_code.get(username))
            time.sleep(3)
            clear()
            exit()
        else:
            print('password error')
            break
    else:
        print('name error // input name again')
