print('Argumentos posicionais')

def pet(pet_type,name):
       print(f'I have a {pet_type} your name is {name}')

pet('hamster','litle')
pet('litle','hamster')
print('...\n')


print('Argumentos nomeados \'keyword arguments\' ')
pet(name = 'litle', pet_type = 'hamster')
pet(pet_type = 'hamster',name = 'litle')
print('...\n')

#=============================================================================
print('Argumentos default')

def pet_padrao(name, pet_type= 'dog'):
       print(f'I have a {pet_type} your name is {name}')

pet_padrao('duque')
print('...\n')
