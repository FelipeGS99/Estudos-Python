i = int(input("Inicio: "))
f = int(input("Fim: "))
print("Os números pares dentro do intervalo {} e {} são:".format(i, f))
for c in range(i, f+1):
    if c % 2 == 0:
        print(c)
