salario = float(input("Digite o seu salário atual: "))
if salario > 1250:
    novosalario = float(salario * 1.1)
    print("Seu salário após o reajuste é de R${:.1f}".format(novosalario))
elif salario <= 1250:
    novosalario = float(salario * 1.15)
    print("Seu salário após o reajuste é de R${:.1f}".format(novosalario))
else:
    print("Salário Inválido")