n,x = map(int, input('n,x=').split())
A = [float(i) for i in input().split()]
d=0
for i in A:
    sailech = abs((i-x)/100)
    if sailech <= 0.05:
        d += 1
print(d)