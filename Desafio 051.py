i = int(input("Digite o ínicio da Progressão aritmética: "))
r = int(input("Digite a razão da Progressão aritmética: "))
print("Progressão aritmética com inicio em {} de razão {}".format(i, r))
for c in range(i, r*10, 4):
    print(c)
