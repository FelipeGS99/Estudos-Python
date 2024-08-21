import random
j = ''
n = c = s = con = 0
r = ''
print("Vamos jogar Par ou Ímpar!")
while True:
    j = str(input("Você escolhe par ou ímpar? [P/I]: ").strip().upper())
    n = int(input("Qual número você deseja jogar?: "))
    c = random.randint(1,10)
    s = n + c
    if s % 2 == 0:
        r = 'P'
        rext = 'Par'
    else:
        r = 'I'
        rext = 'Ímpar'
    if j == r:
        print(f"""Você escolheu {rext} e jogou o número {n}, o computador escolheu o número {c}.
Soma = {s}
Resultado = {rext}
Você Ganhou""")
        con += 1
    else:
        print(f"""Você escolheu {rext} e jogou o número {n}, o computador escolheu o número {c}.
Soma = {s}
Resultado = {rext}
Você Perdeu""")
        break
print(f"Você venceu um total de {con} partidas seguidas")


