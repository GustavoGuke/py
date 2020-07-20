import json

def load_user():
    """ abrindo arquivo com nome do usuario"""

    filename = 'lendoDados.json'

    try:
        with open(filename) as f:
            user = json.load(f)
         
    except FileNotFoundError:
        return None
    except json.decoder.JSONDecodeError:
        print('nenhum usuario salvo favor preencher: ')
        return None
    
    else:
        return user

    
def ifNotExistUser():
    """ Caso não exista o arquivo essa função cria  """
    
    user = input('whats your names? ')
    filename = 'lendoDados.json'
    with open(filename, 'w') as f:
        json.dump(user, f)
    return user
 

def show_user():
    """ Mostar o usuario salvo """
    user = load_user()

    if user:
        print(user)
    else:
        username = ifNotExistUser()

        
show_user() 




