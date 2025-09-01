n = [5, 3, 2, 3, 6, 3, 3]
b = [0] * 10
for i in n:
    b[i] = b[i] + 1

tui = 0
for i in range(len(b)):
    if b[i] >= 4:
        d = b[i] // 4
        s = i * i
        if s > tui:
            tui = s
print(tui, d)
