frase = str(input("Digite uma frase: ")).strip().lower()
print("A letra 'A' aparece {} vezes na frase".format(frase.count("a")))
print("A letra 'A' aparece na frase pela primeira vez na posição {}".format(frase.find("a") + 1))
print("A letra 'A' aparece na frase pela última vez na posição {}".format(frase.rfind("a") + 1))
