sexo = str(input("Digite o seu sexo(M/F): ")).strip().upper()[0]
while sexo not in 'MF':
    print("Entrada Inválida, Tente Novamente!")
    sexo = str(input("Digite o seu sexo(M/F): ")).strip().upper()[0]
print("Entrada Válida")
