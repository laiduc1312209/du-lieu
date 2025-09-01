a = [1,1,2,2,2,1]
n = len(a)
khoang_cach_lon_nhat = 0

for i in range(n):
    for j in range(i + 1, n):
        if a[i] == a[j]:
            khoang_cach = j - i
            if khoang_cach > khoang_cach_lon_nhat:
                khoang_cach_lon_nhat = khoang_cach

print(khoang_cach_lon_nhat)