
ingre =['mushrooms','extra cheese']

if 'mushrooms' in ingre:
    print('mushrooms adicionado')
if 'extra cheese' in ingre:
    print('extra cheese adicionado')
print('\n\n')
#EXERCICIOS====================================================================
print('EXERCICIO #1')
alien_cor = 'verde'

if alien_cor == 'verde':
    print('voce ganhou 5 pontos')
print('\n\n')
#EXERCICIOS====================================================================
print('EXERCICIO #2')
alien = input('DIGITE A COR DO ALIEN: \n'
              'VERDE - 1\n'
              'AMARELO - 2\n'
              'VERMELHO - 3: \n')
if alien == '1':
    print('voce ganhou 5 pontos')
elif alien == '2':
    print('voce ganhou 10 pontos')
elif alien == '3':
    print('voce ganhou 15 pontos')
else:
    print('ERRO NA ENTRADA DE DADOS')


