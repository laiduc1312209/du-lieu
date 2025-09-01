fi=open('SOPDS.INPUT','r')
fo=open('SOPDS.OUTPUT','w')
s=fi.readline()

ds = [1,2,3,4,5,6,7,8,9,10]
n=int(s)
for i in range(11,n**2):
    s = str(i)
    for j in range(len(s)-1):
        tich = int(s[j])*int(s[j+1])
        tong = int(s[j])+int(s[j+1])
        if tong == 0:
            break
        if tich%tong == 0 and s not in ds:
            ds.append(s)
print(ds[n-1],file=fo)
fi.close()
fo.close()