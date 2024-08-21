from time import sleep
i = int(input("Digite o número inicial da contagem regressiva: "))
c = 0
for c in range (i, 0, -1):
    print(c)
    sleep(1)