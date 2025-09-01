def timchuso(x):
    if x in ['1','2','3','4','5','6','7','8','9','0']:
        return True
    else:
        return False
s = input('S = ')
tong = 0
# s = '5trrraann thhhhi45 ttthannh ta64mmm'
smoi = ''
smoimoi = ''
for i in range(len(s)):
    if timchuso(s[i]):
        tong += int(s[i])
    if timchuso(s[i]) == False:
        smoi += s[i]
print(tong)
print(smoi)

for i in range(len(smoi)):
    if smoi[i] != smoi[i-1]:
        smoimoi += smoi[i]
print(smoimoi)