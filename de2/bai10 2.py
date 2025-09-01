fi = open('butchi.inp','r')
N,P,K=fi.readline().split()
n=int(N)
p=int(P)
k=int(K)

n=n-(n//k-1)

a=n*p

print(a)

fi.close()
fo.close()