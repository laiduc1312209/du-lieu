n,H=map(int, input().split())
dsbai = []
for i in range(n):
    bai=[]
    for j in range(1):
        a,b = map(int, input().split())
        bai.append(a)
        bai.append(b)
    dsbai.append(bai)
dsbai.sort(key=lambda x:(x[0],x[1]))
for i in range(n):
    if H>=dsbai[i][0]:
        H = H+dsbai[i][1]
    else:
        break
    
print(H)
