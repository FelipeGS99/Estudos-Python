listanum = []
continua = 'S'
while continua == 'S':
    num = int(input("Digite um número: "))
    if num not in listanum:
        listanum.append(num)
    continua = str(input("Deseja adicionar outro número? [S/N]")).upper()
listanum.sort()
print(listanum)