import json


'''

# Salvando dados em um arquivo

while True:
    
    username = input('whats your name: ')
    if username == 'q':
        break
        
    lastname = input('whats your last name: ')
    if lastname == 'q':
        break
    
    names = {}
    names['name']=username
    names['lastname']=lastname
    


# usando a função json.dump(arquivo a ser salvo, arquivo onde sera salvo)
    filename = 'username.json'
    with open(filename, 'a') as f:
        json.dump([names], f)
        f.write('\n')
        print('Nome Gravado: ' + username)
        
'''

'''

# visualizar o arquivo
filename = 'username.json'
with open(filename, 'r') as f:
    i  = f.read()
    print(i)

'''


filename = 'username.json'
with open(filename, 'r') as f:
    i  = f.read()
    print(i)



