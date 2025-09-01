a = [int(i) for i in input().split()]
for i in range(len(a)-2,-1,-1):
        if a[0]>a[i]:a.pop(0)      
        else:a.pop(len(a)-1)   
print(a)