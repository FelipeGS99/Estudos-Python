valores = list()
maior = 0
menor = 0
for c in range(0, 5):
    valores.append(int(input("Digite um número: ")))
    if c == 0:
        maior = menor = valores[0]
    else:
        if valores[c] > maior:
            maior = valores[c]
        elif valores[c] < menor:
            menor = valores[c]
print(f"O maior número da lista é o número {maior}, encontrado na posição ", end='')
for c, n in enumerate(valores):
    if n == maior:
        print(f'{c}...', end='')
print()
print(f"O menor número da lista é o número {menor}, encontrado na posição ", end='')
for c, n in enumerate(valores):
    if n == menor:
        print(f'{c}...', end='')





