def np(n):
    s = ''
    while n != 0:
        du = n%2
        s = str(du) + s
        n= n//2
    return s
print(np(2009))

# def dx(s):
#     for i in range(len(s)//2+1):
#         if s[i] != s[len(s)-1-i]: return False
#     return True
# print(dx(np(12312)))