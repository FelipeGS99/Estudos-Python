from random import randint
jogos = []
numeros = []
quant = int(input("Quantos jogos deseja gerar?: "))
num = 0
for j in range(0, quant):
    while len(numeros) < 6:
        num = randint(1, 60)
        if num not in numeros:
            numeros.append(num)
    jogos.append(numeros[:])
    numeros.clear()
for j in range(0, quant):
    jogos[j].sort()
    print(f"Jogo {j + 1}: {jogos[j]}")