dist = float(input("Digite a distância da viagem em km: "))
if dist <= 200:
    custo = float(dist * 0.5)
    print("Custo da passagem = R${}".format(custo))
elif dist > 200:
    custo = float(dist * 0.45)
    print("Custo da passagem = R${}".format(custo))
else:
    print("Distância Inválida, a distância deve ser um número positivo.")