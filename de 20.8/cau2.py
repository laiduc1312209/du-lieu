x = int(input())
def fx(x):
    s = str(x)
    tong = 0
    for i in range(len(s)):
        tong += int(s[i])
    return tong
while fx(x) >= 10:
    x=fx(x)
print(fx(x))