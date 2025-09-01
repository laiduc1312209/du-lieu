p,q,r=map(int, input().split())
if p > q and p>r :
    print('An')
elif q > p and q>r :
    print('Vinh')
elif r > p and r>q :
    print('Quang')
elif r == q or r == p or p == q:
    print("BAU LAI")