def gaithua(x):
    gt = 1
    for i in range (1,x+1):
        gt = gt * i
    return gt
c = 0
n = int(input('n='))
n = str(n)
for i in range(len(n)):
    b = int(n[i])
    c = c + gaithua(b)
print(c)