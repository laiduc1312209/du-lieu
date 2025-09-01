fi = open('bai5.inp','r')
fo = open('bai5.out','w')

n = fi.readline()
u,v = fi.readline().split()
s = fi.readline()

print('Số cột là:',n)
print('Điểm bắt đầu là :',u,v)
print('Lệnh di chuyển là:',s)

n = int(n)
u = int(u)
v = int(v)

td1=v+(u-1)*n

for i in range(0,len(s)):
    if s[i] == 'U':
        u = u + 1
        if u == n:
            u = 1
    elif s[i]== 'D':
        u = u - 1
        if u == 1:
            u = n
    elif s[i]== 'R':
        v = v - 1
        if v == 1:
            v = n
    elif s[i]== 'L':
        v = v + 1
        if v==n:
            v= 1
td=v+(u-1)*n

print(td,file=fo)
print('Đích là :', td)
fi.close()
fo.close()