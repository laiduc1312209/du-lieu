h = [int(i) for i in input().split()]
d = int(input())
dem = 0
for i in range(len(h)):
    dau = 0
    cuoi = i - 1
    k = h[i]-d
    co = False
    while dau <= cuoi:
        giua = (dau + cuoi) // 2
        if h[giua] == k:
            co = True
            break
        elif h[giua] < k :
            dau = giua + 1
        else:
            cuoi = giua - 1
    if co == True:
        dem += 1
print(dem)
