n = int(input('n = '))
p = list(map(int, input().split()))

sp = 0
for i in range(len(p)):
    sp += p[i]
spmoi=sp/4

if spmoi > int(spmoi):
    print(int(spmoi)+1)
else:
    print(int(spmoi))