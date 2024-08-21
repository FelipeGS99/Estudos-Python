valorcasa = float(input("Qual o valor da casa?: "))
salario = float(input("Qual o seu salário mensal?: "))
tempo = int(input("Em quantos anos você deseja pagar essa casa?: "))
mensal = valorcasa / (tempo * 12)
if mensal >= salario * 0.3:
    print("Empréstimo Negado")
else:
    print("Empréstimo Aceito")
