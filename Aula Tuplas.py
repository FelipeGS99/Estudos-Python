lanche = 'Arroz', 'Feijão', 'Carne', 'Batata Frita'
# A primeira variável recebe a posição(enumerate) e a segunda variável recebe o conteúdo que está dentro da tupla na posição do enumerate
for pos, comida in enumerate(lanche):
    print(comida, pos)