i = int(input("Inicio: "))
f = int(input("Fim: "))
s = 0
for c in range(i, f+1):
    if c % 2 != 0 and c % 3 == 0:
        s = s + c
print("A soma dos números ímpares e múltiplos de 3, dentro do intervalo {} e {}, é igual a {}".format(i, f, s))


