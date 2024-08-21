from random import randint
from time import sleep
from operator import itemgetter
jogos = {}
for c in range(1, 5):
    jogos[f'Jogador {c}'] = randint(1, 6)
for k, v in jogos.items():
    print(f"{k} tirou {v} no dado.")
    sleep(1)
rank = sorted(jogos.items(), key=itemgetter(1), reverse=True)
#keyitemgetter indica em qual índice o sorted ira ordenar key = 0 no caso seria ordenado a chave('jogador1', 'jogador2' por exemplo), key = 1 ordena os valores dentro da chave
print('=-'*30)
print(f'                      Rankings')
print('=-'*30)
for j, v in enumerate(rank):
    print(f"{j+1}o Colocado: {v[0]}, que tirou {v[1]} no dado.")
    sleep(1)