fi=open('SONT.INPUT','r')
fo=open('SONT.OUTPUT','w')
so = fi.readline()
s = []
def snt(a):
    if a == 1: return False
    if a == 2 or a==3: return True
    for i in range(2,int(a**0.5)+1):
        if a%i == 0 :
            return False
    return True
for j in range(len(str(so))):
    s.append(int(str(so[j])))
kq = []
for i in range(len(s)):
    if snt(s[i]) and s[i] not in kq:
        kq.append(s[i])
print(*kq,file=fo)
fi.close()
fo.close()