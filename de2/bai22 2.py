# fi = ('hotel.inp','r')
# fo = ('hotel.out','w')

# n = fi.readline()
n=int(input())

if n%3==2:
    print(n//3,1)
elif n%3==1:
    print((n//3)-1,2)
else:
    print(n//3,0)


# fi.close()
# fo.close()