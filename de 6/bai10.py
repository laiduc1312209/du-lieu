a = input()
def tp(s,n):
    if n == 1: return int(s[0])
    elif n>1: return (2*tp(s,n-1)+int(s[n-1]))
print(tp(a,len(a)))