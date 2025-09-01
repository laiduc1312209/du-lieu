a = int(input('a='))
b = int(input('b='))
def ucln(x,y):
    if y == 0:
        return x
    return ucln(y,x%y)
ucln = ucln(a,b)
print('UCLN la: ',ucln)
tu = int(a/ucln)
mau = int(b/ucln)


print('Phan so toi gian la:',tu,'/',mau)

scp=''
bt = []
for i in range(a,b+1):
    if (int(i**0.5))**2 == i :
        scp += str(i)+' '
    s = str(i)
    for j in range(len(s)-1):
        if int(s[j]) <= int(s[j+1]):
            bt.append(i)
print('Cac so chunh phuong la:',scp)
print('Co',len(bt),'bac thang')