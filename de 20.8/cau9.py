n = int(input('N='))
b = 0
if 1<=n<=5:
    b = n*6500
    print(b)
    print(b*12/100)
    print(b+b*12/100)

elif 6<=n<=25:
    b = n*7800
    print(b)
    print(b*12/100)
    print(b+b*12/100)
elif 16<=n<=25:
    b = n*9200
    print(b)
    print(b*12/100)
    print(b+b*12/100)
elif n>=25:
    b = n*10300
    print(b)
    print(b*12/100)
    print(b+b*12/100)