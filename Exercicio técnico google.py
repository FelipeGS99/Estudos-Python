numstr = str(input("Digite um número: ")).upper()
contra = ''
for c in range(len(numstr) - 1, -1, -1):
    contra = contra + numstr[c]
print(contra)
if numstr == contra:
    print("O número/palavra é igual de trás pra frente.")
else:
    print("O número/palavra não é igual de trás pra frente.")