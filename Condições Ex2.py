vel = float(input("Digite a velocidade do carro: "))
if vel > 80:
    excesso = float(vel - 80)
    multa = float(excesso * 7.00)
    #multa = (vel - 80) * 7
    print("Velocidade acima dos limites da pista, será cobrada uma multa no valor de R${:.1f}".format(multa))
elif vel > 0 and vel <= 80:
    print("Velocidade dentro dos limítes, nenhuma multa será aplicada!")
else:
    print("Velocidade inválida, a velocidade deve ser um número maior do que 0")