def ucln(x,y):
    if y == 0:
        return x
    return ucln(y,x%y)
a,b=map(int , input('Nhập phân số :').split('/'))

a = a/ucln(a,b)
b = b/ucln(a,b)
print(int(a),'/',int(b))