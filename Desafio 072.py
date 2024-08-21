num = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
i = 0
while True:
    i = int(input("Digite um número de 0 a 20: "))
    while i < 0 or i > 20:
        i = int(input("Entrada Inválida, tente novamente: "))
    print(f'Você digitou o número {num[i]}')