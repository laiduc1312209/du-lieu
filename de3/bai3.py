a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
a.sort()
b.sort()

c = True

for i in range(len(a)):
    if a[i]<=b[i]:
        c=False
        break
if c == True:
    print('Y')
else:
    print('N')