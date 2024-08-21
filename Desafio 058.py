import random
num = random.randint(0,10)
resposta = int(input("Digite qual número você acha que estou pensando: "))
tentativas = 1
while resposta != num:
    resposta = int(input("Resposta errada, tente novamente: "))
    tentativas += 1
print("Parabéns! Você acertou, o número que estava pensando era o {}, você precisou de {} tentativas para acertar.".format(num, tentativas))

