frase = str(input("Digíte uma frase: ")).replace(" ", "").strip().lower()
contra = ''
for c in range(len(frase)-1, -1, -1):
    contra = contra + frase[c]
if frase == contra:
    print("Palíndromo")
else:
    print("Não é um Palíndromo")
