print('Exercicio 7.4\n peça para o cliente digitar os ingredientes da pizza\n'
      ' Quando ele digitar sair pare o programa:')

ativo = True
while ativo:
    ingredientes = input('Quais ingredientes voce quer em sua pizza: ')
    if ingredientes == 'sair':
        ativo = False
    else:
        print('O Ingrediente foi adicionado', ingredientes)
print('...')
print('\n\n')
#==============================================================================

print('Escreva um laço que informe o preço do \n'
      ' ingresso no cinema de acordo com a idade')

ative = 'sim'
while ative == 'sim':
    idade = int(input('Digite sua idade: '))

    if idade < 4:
        print('Entrada gratutita')
    elif idade < 16:
        print('R$ 15,00')
    elif idade >= 16:
        print('R$ 30,00')
    else:
        print('ERRO')

    ative = input('Continuar digite sim/nao para sair: ')
#==============================================================================
print('Faça um codigo infinito')

sempre = 'sim'

while sempre == 'sim':
    print('Python')

#================================= ate pg 179 =================================
        
              
