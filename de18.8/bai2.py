d = 'TOICODOIMATNHINRATTINHTOINHINTHAYNHUNGNGUOIVOHINHBONTOIDUNGBENNHAUSUCMNAHVUNGTRAICUATINHBANTHANNHIEUKHITRAITIMTOIDAPRATNHANHKHONGPHAINHUNGVETTHUONGKHOLANH'
s = 'ABCABDABCDAEF'
nho = []
max = 0
for i in range(len(s)):
    if s[i] not in nho:
        nho.append(s[i])
    elif s[i] in nho:
        if len(nho)>max:
            max = len(nho)
        nho = []
        nho.append(s[i])
print(max)    