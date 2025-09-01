x = [int(i) for i in input().split()]
b=0
def snt(n):
    if n == 1 :
        return False
    if n == 2 :
        return True
    for i in range (2,int(n**0.5)+1):
        if n % i == 0 :
            return False
    return True
for i in x :
    if snt(i)==True: b=b+1
print(b)