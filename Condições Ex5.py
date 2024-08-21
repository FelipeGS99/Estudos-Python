ano = float(input("Digite um ano para saber se ele é bissexto ou não: "))
if ano % 4 == 0:
    print("Ano Bissexto")
elif ano % 4 == 1 or ano % 4 == 2 or ano % 4 == 3:
    print("Não Bissexto")
else:
    print("Ano Inválido")
