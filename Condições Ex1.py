import random
num = random.randint(0, 5)
resposta = int(input("Tente adivinhar qual o número entre 0 e 5: "))
if resposta == num:
    print("Parabéns, você adivinhou o número!")
elif resposta < 0 or resposta > 5:
    print("Resposta inválida. A resposta deve ser um número inteiro entre 0 e 5.")
else:
    print("Resposta errada, o número correto era: {}".format(num))