n = list(map(int, input().split()))
chan = []
le = []

for i in n:
    if i % 2 == 0:
        chan.append(i)
        chan.sort()
    elif i % 2 != 0:
        le.append(i)
        le.sort()
print(chan + le)