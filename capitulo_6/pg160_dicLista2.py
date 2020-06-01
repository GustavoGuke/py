print('Usando listas para armazenar dados dentro de valores de dicionarios')

pizza = {
    'massa': 'crocante',
    'coberturas': ['queijo extra', 'cogumelos'],
    }
print(pizza)
print('...')

print('mudando um dado dentro do dicionario por indice')
if pizza['coberturas'][1]=='cogumelos':
    pizza['coberturas'][1]='ameixa'
    
      
print('A massa sera '+ pizza['massa']+ ' com as cobeturas:')
for i in pizza['coberturas']:
    print('\t',i)
print('\n\n')
#==============================================================================

print('Dicionarios com Lista')

stacks = {
    'jen': ['python','c'],
    'sarah': [ 'java'],
    'phill': ['html', 'css'],
    'jow': ['javascript', 'php'],
    }


for nome, stack in stacks.items():
    if len(stack) == 1:
        print('\n ola ',nome.title(), ' sua liguagem favorita é: ', stack)
    else:
        print('\n',nome.title() + ' linguagem favorita: ', stack[0])
        for i in stack:
            print('\t',i.title())
print('...')






