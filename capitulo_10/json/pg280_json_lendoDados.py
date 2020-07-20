import json

'''
# Salvando dados
user = input('whats your names? ')
filename = 'lendoDados.json'

with open(filename, 'w') as f:
    json.dump(user, f)
    print('User confirmed: '+ user)


# Lendo Dados
filename = 'lendoDados.json'
with open(filename) as f:
    user = json.load(f)
    print('User confirmed: '+ user)

#============================================================================
# codigos acima em um arquivo except

filename = 'lendoDados.json'

try:

    with open(filename) as f:
        user = json.load(f)

except FileNotFoundError:
    user = input('whats your names? ')

    with open(filename, 'w') as f:
        json.dump(user, f)
else:
    print(user)

'''

#============================================================================
# codugo acima em uma função

def greet():
    filename = 'lendoDados.json'
    try:
        with open(filename) as f:
            user = json.load(f)

    except FileNotFoundError:
        user = input('whats your names? ')
        with open(filename, 'w') as f:
            json.dump(user, f)
            
    else:
        print(user)
        
greet()









    
    
