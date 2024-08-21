lista = []
while True:
    nome = str(input("Nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    continua = str(input("Deseja continuar?: ")).upper()
    while continua not in 'SN':
        print("Entrada Invalida!")
        continua = str(input("Deseja continuar?: ")).upper()
    if continua == 'N':
        break
for i, a in enumerate(lista):
    print(f"{i} - {a[0]} - {a[1]} - {a[2]}")