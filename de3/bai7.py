a = [16, 17, 4, 3, 5, 2]
b = []
for i in range(len(a)):
    ld=True
    for j in range(i+1,len(a)):
        if a[i]<=a[j]:
            ld=False
            break
    if ld :
        b.append(a[i])
print(b)
