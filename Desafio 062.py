i = int(input("Digite o ínicio da Progressão aritmética: "))
r = int(input("Digite a razão da Progressão aritmética: "))
print("Progressão aritmética com inicio em {} de razão {}".format(i, r))
PA = i
c = 1
while c <= 10:
    print(PA)
    PA += r
    c += 1
continua = 'S'
while continua in 'S':
    continua = str(input("Deseja continuar a progressão? [S/N]: ")).strip().upper()
    if continua == 'S':
        add = int(input("Por quantos números você deseja que eu continue a progressão?: "))
        while add > 0:
            print(PA)
            PA += r
            add -= 1
    elif continua == 'N':
        print("Fim!")
    else:
        print("Entrada Inválida.")
