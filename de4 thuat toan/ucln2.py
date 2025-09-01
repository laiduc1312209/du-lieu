def ucln(x,y):
    if y == 0:
        return x
    return ucln(y,x%y)
dem = 0
a = list(map(int, input('a = ').split()))
for i in range(len(a)-1):
    for j in range(1,len(a)):
        if ucln(a[i],a[j])==1:
            dem += 1
print(dem)