print('Exercicio 6.7 \n Criar dois novos dicionarios com o dic da pag147'
      ' percorrer\n com um laço e apresentar cada uma das pessoas:')

pessoa = {
    'first_name': 'Gustavo',
    'last_name': 'Silva',
    'age': 25,
    'city': 'Atuja',
    }
pessoa1 = {
    'first_name': 'Kerolin',
    'last_name': 'Lima',
    'age': 25,
    'city': 'Atuja',
    }
pessoa2 = {
    'first_name': 'Joao',
    'last_name': 'Lima',
    'age': 10,
    'city': 'Atuja',
    }

people = [pessoa,pessoa1,pessoa2]

for p in people:
    fullName = p['first_name']+ ' '+ p['last_name']
    idade = p['age']
    cid = p['city']
    
    print('Nome:',fullName)
    print('\t Cidade:',cid)
    print('\t Idade:',idade)
#============================================================================  

        

 
        
