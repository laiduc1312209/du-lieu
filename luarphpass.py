passinput = input('Enter your pass:')
pass_leght=len(passinput)
convert_pass = []
for i in range(pass_leght):
    convert_pass.append(passinput[i])
    convert_pass.append(passinput[-i-1])
    if len(convert_pass)==pass_leght:break 
print(convert_pass)

