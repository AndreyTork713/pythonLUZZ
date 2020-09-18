# ЗАмок с управлением по числовому паролю

import time
import dop

el = input('Enter ON or OFF')

dop.el_automat(el)

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
    elif password == (3105704888):
        lock = 1
        print('Программа остановлена, дверь разблокирована')
        time.sleep(5)
        password = ()
        electro = 0
    else:
        print('не верный пароль, дверь закрыта')
