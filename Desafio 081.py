lista = []
continua = ''
while True:
    lista.append(int(input("Digite um número: ")))
    continua = str(input("Deseja adicionar outro número?: [S/N]")).upper()
    while continua not in 'SN':
        print("Entrada Inválida!")
        continua = str(input("Deseja adicionar outro número?: [S/N]")).upper()
    if continua == 'N':
        break
print(f"Foram digitados {len(lista)} números.")
listainvertida = lista[:]
listainvertida.sort(reverse = True)
print(f"Lista em ordem decrescente: {listainvertida}")
if 5 in lista:
    print("O número 5 está presente na lista nas posições: ", end='')
    for c, n in enumerate(lista):
        if n == 5:
            print(f"{c}...", end='')
else:
    print("O número 5 não está presente na lista.")


