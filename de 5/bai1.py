def snt(a):
    if a == 1: return False
    if a == 2 or a==3: return True
    for i in range(2,int(a**0.5)+1):
        if a%i == 0 :
            return False
    return True

n = int(input('n = '))
s = str(n)
tong = 0
tong2 = 0
min = 0
for i in range(len(s)):
    tong = int(s[i])+tong
for i in range(1,n+1):
    if snt(i):
        tong2 = tong2 + i
        if i > min :
            min = i
print(len(s))
print(tong)
print(tong2)
print(min)