import json

# exercicio 10.13
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





def other_user():
    """ Troca o nome do usuario """
    
    new_user = input('Se deseja trocar o usuario digite (s/n): ')
    if new_user == 's':
        user_new = ifNotExistUser()
    elif new_user == 'n':
        print('usuario não trocado')
    else:
        print('Digite apenas: s para sim , n para nao')




def show_user():
    """ Mostar o usuario salvo """
    
    user = load_user()
    if user:
        print(user)
        new_user = other_user()        
    else:
        username = ifNotExistUser()
        
           
show_user() 




