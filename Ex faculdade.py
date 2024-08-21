matriz = []
tamanho = int(input("Digite quantos números deseja adicionar na matriz: "))
inv = 0
for c in range(0, tamanho):
    matriz.append(int(input("Número para a posição {} da matriz: ".format(c))))
    if matriz[c] < matriz[c-1]:
        inv = inv + 1
print("Inversões = {}".format(inv))