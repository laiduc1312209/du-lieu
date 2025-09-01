n = int(input())
def hat(n):
    if n == 0: 
        print('Mua them')
        
    if n == 1: 
        print('An not')
        hat(n-1)
    if n >= 2:
        print('co',n,'keo','lay 1 ra an')
        print('con',n-1,'keo')
        hat(n-1)
hat(n)