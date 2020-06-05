print('Exercicio 7.8')
print('fazer uma lista com pedido de sanduiches apresentar eles na Tela\n'
      'depois coloca-los em outra lista e aprensentar usando while:')

ordem_sanduba = ['x-salada','x-burguer','x-bacon','x-tudo']

sanduba_feitos = []

while ordem_sanduba:
    fazendo = ordem_sanduba.pop()
    print('Estamos preparando:',fazendo)

    sanduba_feitos.append(fazendo)
for sanduba_prontos in sanduba_feitos:
    print('Preparado:',sanduba_prontos)
print('...')
print('\n\n')
#==========================================================================
print('Exercicio 7.9')
print('Garanta que um sanduiche apareça mais de uma vez na lista\n'
      'eo msm seja retirado com um laço while apresentando uma msg:')

ordem_sanduba = ['x-salada','x-burguer','x-salada','x-tudo','x-salada']
sanduba_feitos = []


while ordem_sanduba:
    while 'x-salada' in ordem_sanduba:
        remove = ordem_sanduba.remove('x-salada')
    fazendo = ordem_sanduba.pop()
    print('Estamos sem ingredientes para fazer x-salada')


    sanduba_feitos.append(fazendo)
for sanduba_prontos in sanduba_feitos:
    print('Preparado:',sanduba_prontos)
print('...')
print('\n\n')
#=============================================================================
print('Exercicio 7.10')
print('Fazer uma enquete de video- games e mostar seu melhores jogos')

games = {}

ativo = True

while ativo:
    console = input('Digite o console: ')
    jogo = input('Digite o melhor jogo que você acha desse console: ')


    games[console]=jogo

    outro_console = input('Digite um segundo console que você tambem goste\n'
                          '(s/n): ')
    if outro_console == 'n':
        ativo = False

print('Pesquisa melhores jogos')
for console, jogos in games.items():
    print('Console: ',console)
    print('Jogos: ', jogos)
print(games)
