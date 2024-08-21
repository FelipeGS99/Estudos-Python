i = int(input("Digite o ínicio da Progressão aritmética: "))
r = int(input("Digite a razão da Progressão aritmética: "))
print("Progressão aritmética com inicio em {} de razão {}".format(i, r))
PA = i
c = 1
while c <= 10:
    print(PA)
    PA += r
    c += 1
