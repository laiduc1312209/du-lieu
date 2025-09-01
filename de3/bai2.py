n,m  = map(int, input().split())
a = [int(i) for i in input().split()]
smin=0
smax=0
a.sort()
for i in range(0,n-m):
    smin += a[i]
a.reverse()
for i in range(0,n-m):
    smax += a[i]
print(smax-smin)