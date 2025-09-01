a,b,c,d=map(int, input().split())
lan = []
if a<b:
    for i in range(a,b+1):
        lan.append(i)
if c<d:
    for i in range(c,d+1):
        if i not in lan:
            lan.append(i)
print(len(lan))