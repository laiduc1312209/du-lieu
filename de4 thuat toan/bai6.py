In = int(input())
a = ['0','1']
s = str(In)
dem = 0
for i in range(len(s)):
    if s[i] not in a :
        dem +=1
print(dem)