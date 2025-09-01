n = [int(i) for i in input().split()]
max_zeros = 0
current = 0

for i in n:
    if i == 0:
        current += 1
        if current > max_zeros:
            max_zeros = current
    else:
        current = 0

print(max_zeros)
