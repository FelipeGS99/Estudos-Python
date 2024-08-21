nome = str(input("Digite seu nome completo: ")).strip().title()
print("Nome Completo: {}".format(nome))
nomesep = nome.split()
print("Seu primeiro nome é {}".format(nomesep[0]))
print("Seu último nome é: {}".format(nomesep[len(nomesep) - 1]))
#nomesep[len(nomesep) - 1] significa lista na posição len(comprimento) - 1, ou seja, na última posição da lista
