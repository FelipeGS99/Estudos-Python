nome = str(input("Digite seu nome completo: ")).strip()
print("Seu nome em letras maiúsculas é {}".format(nome.upper()))
print("Seu nome em letras minúsculas é {}".format(nome.lower()))
print("Seu nome contém {} letras".format(len(nome) - nome.count(" ")))
nomeseparado = nome.split()
print("Seu primeiro nome contém {} letras".format(len(nome[0])))
print(nomeseparado)