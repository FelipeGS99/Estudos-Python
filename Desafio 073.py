times = 'Palmeiras', 'Botafogo', 'Grêmio', 'Bragantino', 'Atlético Mineiro', 'Flamengo', 'Athletico-PR', 'Fluminense', 'Cuiabá', 'São Paulo', 'Corinthians', 'Fortaleza', 'Internacional', 'Santos', 'Vasco Da Gama', 'Bahia', 'Cruzeiro', 'Goiás', 'Coritiba', 'América-MG'
print('-='*60)
print(f'Os 5 primeiros colocados do Campeonato Brasileiro são:')
for time in range(0, 5):
    print(times[time])
print('-='*60)
print(f'Os 4 últimos colocados do Campeonato Brasileiro são: {times[-4:]}')
for time in range(16, len(times)):
    print(times[time])
print('-='*60)
print(f'Lista dos participantes em ordem alfabética: ')
ordem = sorted(times)
for time in ordem:
    print(time)
print('-='*60)
print(f'O time do São Paulo está na posição de número {times.index("São Paulo") + 1}')