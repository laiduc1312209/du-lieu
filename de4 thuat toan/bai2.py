def dx(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s)-1-i]: return False
    return True
def np(n):
    s = ''
    while n != 0:
        du = n%2
        s = str(du) + s
        n= n//2
    return s
def snt(a):
    if a == 1: return False
    if a == 2 or a==3: return True
    for i in range(2,int(a**0.5)+1):
        if a%i == 0 :
            return False
    return True

for i in range(100,1000):
    if snt(i) and dx(str(i)) and dx(np(i)):
        print(i)