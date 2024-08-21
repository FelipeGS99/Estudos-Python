num = int(input("Digite um número para receber o seu resultado fatorial: "))
ante = num - 1
fatorial = num * ante
ante = ante - 1
while ante > 0:
    fatorial = fatorial * ante
    ante = ante - 1
print(fatorial)