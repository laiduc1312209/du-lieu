p,q = map(int, input().split()) #A
r,s = map(int, input().split()) #B
u,v = map(int, input().split()) #C
a,b,c=0,0,0
if q>p :
    b=b+3
elif p>q:
    a=a+3
else:
    a=a+1
    b=b+1

if r>s :
    b=b+3
elif s>r:
    c=c+3
else:
    b=b+1
    c=c+1

if u>v :
    a=a+3
elif p>q:
    c=c+3
else:
    c=c+1
    a=a+1

print(a,b,c)