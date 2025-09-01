from math import sqrt
x,y = map(int, input().split()) #A
u,v = map(int, input().split()) #C
u,y #B
x,v #D

ab = sqrt(((u-x)**2)+((y-y)**2))
ac = sqrt(((x-x)**2)+((v-y)**2))
if ab==ac :
    print('hv')
else:
    print('hcn')