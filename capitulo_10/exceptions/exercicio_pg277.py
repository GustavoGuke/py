# Exercicio 10.6
print('TypeError')
'''
def soma(num1, num2):
    """ somar dois numeros """

    try:
        soma = int(num1) + int(num2)
    
    except TypeError:
        print('Apenas numeros por favor')
    
    except ValueError:
        print('Apenas numeros')
    
    else:
        print(soma)

soma('3','ola')

'''
#========================================================================
# Exercicio 10.7
print('\n')
while True:

    print('Soma dois numeros: ')
    print('aperte (q) para sair:')
    num1 = input('\nPrimeiro Numero: ')
    if num1 == 'q':
        break

    num2 = input('Segundo Numero: ')
    if num2 == 'q':
        break

    try:
        soma = int(num1) + int(num2)

    except ValueError:
        print('\nApenas Numero:(0123456789)\n',
              'Letras nao são aceitas (a/z)\n', 
              'caracter especiais não sao aceitos (@#$%&¨*) \n')

    else:
        print(soma)





