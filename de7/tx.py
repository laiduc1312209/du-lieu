from random import *
import time
tien = 1000
while tien != 0:
    print('TIEN:',tien)
    player = input('Nhap t or x : ')
    cuoc = input('Tien cuoc (all) : ')
    if cuoc == 'all':
        cuoc == tien
    else:
        cuoc == int(cuoc)
    tien = tien-int(cuoc)
    xx1 = randint(1,6)
    xx2 = randint(1,6)
    xx3 = randint(1,6)

    print(xx1)
    time.sleep(1)
    print(xx2)
    time.sleep(1)
    print(xx3)
    time.sleep(1)
    tong = xx1 + xx2 +xx3
    if 3 <= tong <= 10 :
        kqq = 'x'
    else:
        kqq = 't'
    if player == kqq:
        print('win')
        tien = tien + int(int(cuoc)*1.9)
    else:
        print('thua')