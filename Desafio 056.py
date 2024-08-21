nome = ''
lista = ''
for c in range(0, 4):
    print("Pessoa {}".format(c+1))
    nome = str(input("Nome: "))
    lista += nome
lista = lista.split()
print(lista)