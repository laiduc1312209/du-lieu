def gaithua(x):
    gt = 1
    for i in range (1,x+1):
        gt = gt * i
    return gt
def tohop(k,n):
    ckn = gaithua(n)/((gaithua(n-k))*gaithua(k))
    return ckn
a = int(input('n='))
b = int(input('k='))
print('C(',a,',',b,') = ',tohop(b,a))