a,b = 3,3 #map(int, input().split())
diem = 0
for i in range(2):
    if a>b:
        diem += a
        a = a-1
    else:
        diem += b
        b = b -1
print(diem)