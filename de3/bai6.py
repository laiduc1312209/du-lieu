a = [2,5,1,8]
m = a[0]
nha=1
for i in range(len(a)):
    if a[i] > m :
        m = a[i]
        nha +=1
print(nha)