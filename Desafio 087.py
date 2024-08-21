matriz = [[0,0,0], [0,0,0], [0,0,0]]
valor = pares = impares = soma = maiorlinha2 = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f"Digite um valor para a posição [{linha}, {coluna}]: "))
        if matriz[linha][coluna] % 2 == 0:
            pares += matriz[linha][coluna]
        else:
            impares += matriz[linha][coluna]
        if coluna == 2:
            soma += matriz[linha][coluna]
        if linha == 1:
            if matriz[linha][coluna] > maiorlinha2:
                maiorlinha2 = matriz[linha][coluna]
for l in range(0, 3):
    for c in range(0, 3):
        #Com o comando :^5 o programa vai mostrar 5 digitos centralizados
        print(f"[{matriz[l][c]:^5}]", end='')
    print()
print(f"Soma de todos os valores pares digitados: {pares}")
print(f"Soma de todos os valores impares digitados: {impares}")
print(f"Soma dos valores da terceira coluna: {soma}")
print(f"Maior valor da segunda linha: {maiorlinha2}")