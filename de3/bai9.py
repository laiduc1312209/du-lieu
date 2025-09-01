a = [6,5,6,7]
b= []
for i in range(len(a)):
    if a[i] not in b :
        b.append(a[i])
    so=len(b)
print(so)