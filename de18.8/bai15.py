n = int(input('n = '))
ds=[int(i) for i in range(1,n+1)]
kq = []
for i in range(1,n+1):
    kqc = []
    for j in range(i):
        kqc.append(ds[j])
    kq.append(kqc)

print(kq)