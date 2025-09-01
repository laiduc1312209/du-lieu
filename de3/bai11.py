a = [int(i) for i in input().split()]
b=0
dem = 0
for i in range(len(a)-2,-1,-1):
        if a[0] != a[i]:b=len(a)     
        else:b= len(a)-i-1
print(b)