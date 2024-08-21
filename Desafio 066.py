c = s = 0
while True:
    num = int(input("Digite um número inteiro (999 para parar): "))
    if num == 999:
        break
    c += 1
    s += num
print(f"A soma dos {c} números digitados é {s}")

