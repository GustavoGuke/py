
print('Verificando  se uma pessoa participou de uma enquete')

devs = ['jen','sarah','edward','phil', 'erin']

favorite_languages = {'jen':'python',
                      'sarah':'c',
                      'edward':'ruby',
                      'phil':'python'
                      }
for dv in devs:
    if dv not in favorite_languages.keys():
        print('\n',dv.title()+' Please take our poll!' )
    if dv in favorite_languages.keys():
        print(dv.title()+' Thanks for you participate')
print('\n')
#=============================================================================

print('Dicionario ordenado')
for name in sorted(favorite_languages.keys()):
    print(name.title()+ ' thanks')
print('\n')
#=============================================================================

print('Imprimindo apenas os valores')
for v in favorite_languages.values():
    print(v)
print('\n')
#=============================================================================

print('Para Tirar a duplicidade usar metodo set()')

for v in set(favorite_languages.values()):
    print(v)


