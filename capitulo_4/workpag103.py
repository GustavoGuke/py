#TRABALHANDO COM LISTAS

#vizualizando minha lista solicitando apenas indices []
games = ['sub zero', 'scorpiun', 'shao khan']
print(games[0:],'\n')


for i in games[0:]:
    print(i.title())
print('\n')

#COPIANDO UMA LISTA
game_vs = games[:]
print(game_vs)
print('\n')

#PARA MOSTRAR QUE TEMOS DUAS LISTAS DISTINTAS ACRESCENTAR UM ITEM EM CADA UMA
game_vs.append('mestre kame')
games.append('goku')
print(game_vs)
print(games)

