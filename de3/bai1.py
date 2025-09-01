k = int(input('K = '))
n = [int(i) for i in input().split()]
a=0
# for i in n :
#     s=str(i)
#     for j in range(0,len(s)):
#         if s[j] == str(k):
#             a += 1
# print(a)

for i in n :
    while i != 0:
        if i%10 == k : a += 1
        i=i//10
print(a)