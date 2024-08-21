n = int(input("Digite um número: "))
d = 0
for c in range(1, 11):
    if n % c == 0:
        d = d + 1
if n > 1 and d >= 3:
    print("O número {} não é primo".format(n))
else:
    print("O número {} é primo".format(n))