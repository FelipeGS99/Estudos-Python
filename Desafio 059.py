num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
menu = int(input("""[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Digite qual operação deseja realizar: """))
while menu != 5:
    if menu == 1:
        print("A soma entre {} e {} é igual a: {}".format(num1, num2, num1 + num2))
    elif menu == 2:
        print("A multiplicação entre {} e {} é igual a: {}".format(num1, num2, num1 * num2))
    elif menu == 3:
        if num1 > num2:
            print("O maior número digitado é {}".format(num1))
        else:
            print("O maior número digitado é {}".format(num2))
    elif menu == 4:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
    else:
        print("Entrada Inválida")
    menu = int(input("""[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Digite qual operação deseja realizar:"""))
print("Fim!")
