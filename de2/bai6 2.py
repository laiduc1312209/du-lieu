kg = int(input('Nhap so kg gao : '))
bao = [20,10,5,2,1]
d=0
for i in bao:
    if kg >= i:
        d=d+kg//i
        print('Bao',i ,'kg :',kg//i)
        kg=kg%i