produtos = 'Vinho...............', 10, 'Coca-Cola...........', 5, 'Bis.................', 6, 'Carne...............', 20, 'Yakult..............', 1, 'Bala................', 0.5
print('-'*60)
print('                     Listagem de Preços')
print('-'*60)
c = 0
while c <= len(produtos) - 1:
    print(f'{produtos[c]}R${produtos[c+1]}')
    c += 2
print('-'*60)
