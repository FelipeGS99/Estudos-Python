quant = int(input("Digite quantos números da sequência você deseja ver: "))
num1 = 0
num2 = 1
print("{} --> {}".format(num1, num2), end='')
c = 1
while c <= quant:
    prox = num1 + num2
    print(" --> {}".format(prox), end='')
    num1 = num2
    num2 = prox
    c += 1
