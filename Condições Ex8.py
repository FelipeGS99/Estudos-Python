num1 = float(input("Digite o comprimento da primeira reta: "))
num2 = float(input("Digite o comprimento da segunda reta: "))
num3 = float(input("Digite o comprimento da terceira reta: "))
if num1 < num2 + num3 and num2 < num1 + num3 and num3 < num1 + num2:
    print("É possível formar um triâmgulo!")
else:
    print("Não é possível formar um triângulo")