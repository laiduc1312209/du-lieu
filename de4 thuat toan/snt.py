def snt(a):
    if a == 1: return False
    if a == 2 or a==3: return True
    for i in range(2,int(a**0.5)+1):
        if a%i == 0 :
            return False
    return True

#bai1

# n = int(input('n='))
# d=0
# for i in range(0,n+1):
#     if snt(i):
#         print(i)

#bai2

# for i in range(10000,100000):
#     if snt(i):
#         print(i)

#bai3

# l = int(input('L='))
# r = int(input('R='))
# d=0
# for i in range(l,r+1):
#     if snt(i):
#         print(i)

#bai4

n = int(input('n='))
for i in range(n,n+100):
    if snt(i):
        if i > n:
            print(i)
            break


#bai 5

# n = int(input('n='))
# for i in range(n,999999):
#     if snt(i):
#         if i%n == 0:
#             print(i)
#             break