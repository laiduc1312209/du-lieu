n = int(input('n='))
ds = [int(i) for i in input().split()]
min = n+1
ds.insert(0,1)
ds.append(1)
for i in range(len(ds)):
    if ds[i-1]==1 and ds[i]==0:
        dau = i
    if ds[i]==0 and ds[i+1]==1:
        cuoi=i
        kq = cuoi-dau+1
        if kq<min:min=kq
print(min)