from random import randint
print("""0 - Pedra
1 - Papel
2 - Tesoura""")
jogada1 = int(input("Qual é a sua jogada?: "))
jogada2 = randint(1, 3)
itens = ("Pedra", "Papel", "Tesoura")
if jogada1 == jogada2:
    print("Empate")
elif jogada1 == 0 and jogada2 == 1:
    print("Derrota")
elif jogada1 == 0 and jogada2 == 2:
    print("Vitória")
elif jogada1 == 1 and jogada2 == 0:
    print("Vitória")
elif jogada1 == 1 and jogada2 == 2:
    print("Derrota")
elif jogada1 == 2 and jogada2 == 1:
    print("Vitória")
else:
    print("Derrota")
print("Você jogou {}, e o computador jogou {}".format(itens[jogada1], itens[jogada2]))

