def sdx(s):
    for i in range(len(s)//2):
        if s[i]!=s[len(s)-1-i]: return False
    return True
for i in range (101,47000):
    
    if sdx(str(i)) and sdx(str(i*i)):
        print(i,i*i)