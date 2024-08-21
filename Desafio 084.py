galera = []
dados = []
continua = 'S'
contp = 0
peso = []
while continua == 'S':
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Peso: ")))
    galera.append(dados[:])
    dados.clear()
    contp += 1
    continua = str(input("Deseja adicionar outra pessoa? ")).upper()
    while continua != 'S' and continua != 'N':
        print("Entrada Inválida!")
        continua = str(input("Deseja adicionar outra pessoa? ")).upper()
for p in galera:
    peso.append(p[1])
peso.sort()
print(f"Foram cadastradas {contp} pessoas.")
maiorpeso = menorpeso = 0
maiorpeso = peso[len(peso) - 1]
menorpeso = peso[0]
print(f"O maior peso foi de {maiorpeso}Kg, peso de ", end='')
for p in galera:
    if p[1] == maiorpeso:
        print(p[0], end=' ')
print()
print(f"O menor peso foi de {menorpeso}Kg, peso de ", end='')
for p in galera:
    if p[1] == menorpeso:
        print(p[0], end=' ')