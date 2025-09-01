def lomuto(a,dau,cuoi):
    chot = a[cuoi]
    i = dau - 1
    for j in range(dau,cuoi):
        if a[j] <= chot:
            i+=1
            a[i],a[j] == a[j],a[i]
        i += 1
        a[j], a[cuoi] = a[cuoi],a[j]
    return i
def quick_short(a,dau,cuoi):
    if dau < cuoi:
        vitri_tach = lomuto(a,dau,cuoi)
        quick_short(a,dau,vitri_tach-1)
        quick_short(a,vitri_tach+1,cuoi)
a = [[1,2],[4,5],[6,1]]
quick_short(a,0,len(a)-1)
print(a)