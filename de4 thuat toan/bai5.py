def snt(n):
    a = [True for i in range(n+1)]
    a[0] = a[1] = False
    for i in range(2, int(n**0.5) + 1):
        if a[i]:
            for j in range(i*i, n+1, i):
                a[j] = False
    return a

bang_snt = snt(200)

dau = 50
cuoi = 90
for i in range(dau, cuoi + 1):
    if bang_snt[i]:
        s = str(i)
        for j in range(len(s) - 1):
            tong = int(s[j]) + int(s[j+1])
            if bang_snt[tong]:
                print(i)