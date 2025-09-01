def np(n):
    s = ''
    while n != 0:
        du = n%2
        s = str(du) + s
        n= n//2
    return s