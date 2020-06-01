users ={
    'aeinstein':{
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    
    'mcurie':{
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }

print('obtendo informações dos dicionarios')
for userName, userInfo in users.items():
    print('\n Nome: '+ userName)
    fullName = userInfo['first']+ ' ' + userInfo['last']
    location = userInfo['location']
    print('\t Nome completo: '+ fullName)
    print('\t Localizaçao: '+ location)
print('....')


for names, info in users.items():
    print('\n Nome: ',names, '\n Informaçoes: ', info)

