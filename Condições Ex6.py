num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
if num1 >= num2 and num1 >= num3:
    maior = num1
elif num2 >= num1 and num2 >= num3:
    maior = num2
elif num3 >= num1 and num3 >= num2:
    maior = num3
if num1 <= num2 and num1 <= num3:
    menor = num1
elif num2 <= num1 and num2 <= num3:
    menor = num2
elif num3 <= num1 and num3 <= num2:
    menor = num3

print("O menor número é o {} e o maior número é o {}".format(menor, maior))

