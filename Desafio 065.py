num = int(input("Digite um número inteiro: "))
soma = num
maior = num
menor = num
c = 1
continua = str(input("Deseja digitar outro número? [S/N]")).strip().upper()
while continua != 'S' and continua != 'N':
    print("Entrada Inválida.")
    continua = str(input("Deseja digitar outro número? [S/N]")).strip().upper()
while continua == 'S':
    numcont = int(input("Digite um número inteiro: "))
    soma += numcont
    c += 1
    if numcont > maior:
        maior = numcont
    if numcont < menor:
        menor = numcont
    continua = str(input("Deseja digitar outro número? [S/N]")).strip().upper()
print(f"A média dos números digitados é igual a {soma/c}, sendo que {maior} foi o maior número digitado e {menor} foi o menor número digitado.")
