from math import gcd
fi=open('bai1.txt','r')
fo=open('bai11.txt','w')
a,b=fi.readline().split()
c,d=fi.readline().split()
tu1=int(a)
mau1=int(b)
tu2=int(c)
mau2=int(d)
bcnn = (mau1*mau2)/gcd(mau1,mau2)
tum1 = (bcnn/mau1)*tu1
tum2 = (bcnn/mau2)*tu2
tu = tum1 + tum2
print(int(tu), int(bcnn),file=fo)
print(tu)
fo.close()
fi.close()