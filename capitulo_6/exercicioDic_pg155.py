print('imprimir um glossario com um laço for')
glossario = {
    'if':'condicional',
    'case':'condicional',
    'for':'laço',
    'while':'laço',
    'print':'impressao'
    }
for key, value  in glossario.items():
    print('key:',key,'\n value:',value)
print('\n')
#============================================================================

print('acrescentar dados no dicionario')   
glossario['sort']= 'ordenar'
glossario['reverse']= 'invert'
glossario['pop']= 'deleta'

for key, value  in glossario.items():
    print('key:',key,'\n value:',value)
print('\n')
#============================================================================

print('fazer um dicionario e interagir com seus dados') 
rios = {
    'Brasil':'amazonas',
    'Egito': 'nilo',
    'Alemanha':'elba'
    }
for pais,rio in rios.items():
    print('O rio '+rio.title()+ ' fica no '+pais.title())
print('\n')
#===========================================================================

print('Verificando  se uma pessoa participou de uma enquete')

devs = ['jen','sarah','edward','phil', 'erin']

favorite_languages = {'jen':'python',
                      'sarah':'c',
                      'edward':'ruby',
                      'phil':'python'
                      }
for i in devs:
    if i in favorite_languages:
        print('Obrigado por responder Sr '+i)
    if i not in favorite_languages:
        print('favor responder a enquete Sr '+i)



