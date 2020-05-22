
print('Percorrendo dicionário com laço')

user = {
    'userName':'Pytonista',
    'FirstName':'Gustavo',
    'LastName':'Silva'
    }
for key, value in user.items():
    print('Key: ' + key)
    print('Value: ' + value,'\n')
print('\n\n')
#==============================================================================
stack = {
     'Academy':'Python',
     'Udemy':'HTML',
     'Innovation':'Angular',
     'Youtube':'JavaScript'
      }
#print(stack)
for plataform, course in stack.items():
    print('School: ' + plataform)
    print('Language: ' + course,'\n')
#==============================================================================
print('Trazendo apenas as Chaves')
for school in stack.keys():
    print(school)
print('\n')
#==============================================================================
print('Acessando chave e valor em um laço ')
schools = ['Youtube','Udemy']
for key in stack.keys():
    #print(key)
    if key in schools:
        print('Schools Favorites ' + key +
              ' your favorites languages is ' + stack[key])
#=========================== pg 152 ===========================================
