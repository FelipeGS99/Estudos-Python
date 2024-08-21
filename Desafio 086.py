matriz = [[0,0,0], [0,0,0], [0,0,0]]
valor = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f"Digite um valor para a posição [{linha}, {coluna}]: "))
for l in range(0, 3):
    for c in range(0, 3):
        #Com o comando :^5 o programa vai mostrar 5 digitos centralizados
        print(f"[{matriz[l][c]:^5}]", end='')
    print()