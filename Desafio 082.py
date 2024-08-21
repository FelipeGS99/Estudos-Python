lista = []
pares = []
impares = []
while True:
    lista.append(int(input("Digite um número: ")))
    continua = str(input("Deseja adicionar outro número?: [S/N]")).upper()
    while continua not in 'SN':
        print("Entrada Inválida!")
        continua = str(input("Deseja adicionar outro número?: [S/N]")).upper()
    if continua == 'N':
        break
for num in lista:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
lista.sort()
pares.sort()
impares.sort()
print(lista)
print(pares)
print(impares)
