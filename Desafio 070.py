continua = nome = menornome = ''
preço = soma = acima1k = menor = 0
while continua != 'N':
    nome = str(input("Digite o Nome do Produto: ")).upper().strip()
    preço = float(input("Digite o Preço do Produto: "))
    soma += preço
    if preço >= 1000:
        acima1k += 1
    if preço <= menor or menor == 0:
        menor = preço
        menornome = nome
    continua = str(input("Deseja registrar outro Produto? [S/N]: ")).upper().strip()
    while continua not in 'SN':
        print("Entrada Inválida")
        continua = str(input("Deseja registrar outro Produto? [S/N]: ")).upper().strip()
print(f"""Fim da compra!
Total: R${soma}
Quantidade de Produtos acima de R$1000 reais: {acima1k}
Nome do Produto mais barato: {menornome}""")


