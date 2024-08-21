num = 0
soma = 0
c = 0
while num != 999:
    num = int(input("Digite um número diferente de 999: "))
    soma += num
    c += 1
print("A soma dos números digitados é igual a {}. Foram digitados {} números.".format(soma - 999, c - 1))
