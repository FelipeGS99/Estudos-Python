ano = 0
maior = 0
for c in range(0, 7):
    ano = int(input("Digite o ano de seu nascimento: "))
    if 2023 - ano >= 18:
        maior = maior + 1
print("O número de pessoas que já atingiram a maioridade é de {} pessoas!".format(maior))
