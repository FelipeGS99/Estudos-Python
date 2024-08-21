pessoa = {}
pessoa['Nome'] = str(input('Nome: '))
ano = int(input('Ano de Nascimento: '))
contr = aposenta = dif = 0
pessoa['Idade'] = 2023 - ano
pessoa['CTPS'] = int(input('Carteira de Trabalho(0 caso não tenha): '))
if pessoa['CTPS'] == 0:
    for k, v in pessoa.items():
        print(f"{k}: {v}")
elif pessoa['CTPS'] != 0:
    pessoa['Ano de Contratação'] = int(input('Ano de Contratação: '))
    pessoa['Salário'] = float(input('Salário: '))
    contr = 2023 - pessoa['AnoContratação']
    dif = 35 - contr
    aposenta = pessoa['Idade'] + dif
    pessoa['Aposenta com'] = aposenta
    for k, v in pessoa.items():
        print(f"{k}: {v}")