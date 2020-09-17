# ЗАмок с управлением по числовому паролю

import time

lock = 0
electro = 1
while electro == 1:
    print('Введите пароль: ')
    pass1 = int(input())

    password = (pass1)
    if password == (2865):
        lock = 1
        print('дверь открыта')
        time.sleep(5)
        password = ()
        lock = 0
    else:
        print('не верный пароль, дверь закрыта')

