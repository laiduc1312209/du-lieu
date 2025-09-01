a = list(map(int, input().split()))
s=0
b = []
for i in a :
    s=s+i
    b.append(s)
print(b)
for i in range(len(b)):
    if b[i-1]==b[len(b)-1]-b[i]:
        print(i)