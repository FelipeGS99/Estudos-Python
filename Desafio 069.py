adulto = homem = mulher20 = 0
pessoas = 1
continua = ''
while True:
    i = int(input("Digite a sua idade: "))
    while i not in range(0, 1000):
        print("Entrada Inválida, tente novamente!")
        i = int(input("Digite a sua idade: "))
    s = str(input("Digite o seu sexo [M/F]: ")).upper().strip()
    while s != 'M' and s != 'F':
        print("Entrada Inválida, tente novamente!")
        s = str(input("Digite o seu sexo [M/F]: ")).upper().strip()
    if i >= 18:
        adulto += 1
    if s == 'M':
        homem += 1
    if s == 'F' and i >= 20:
        mulher20 += 1
    continua = str(input("Deseja cadastrar outra pessoa? [S/N]: ")).upper().strip()
    if continua == 'N':
        break
    elif continua != 'S' and continua != 'N':
        while continua != 'S' and continua != 'N':
            print("Entrada Inválida")
            continua = str(input("Deseja cadastrar outra pessoa? [S/N]: ")).upper().strip()
print(f"{adulto} pessoas acima de 18 anos foram cadastradas.")
print(f"{homem} homens foram cadastrados.")
print(f"{mulher20} mulheres acima de 20 anos foram cadastradas.")


