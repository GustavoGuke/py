# Argumentos nomeados arbitrários

print('user_profile.py')

def build_profile(first, last, **user_info):
    """ Constrói um dicionário contendo tudo que sabemos de um usuário """

    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last


    # Dicionario criado atraves dos '**'
    print(user_info)
    for key, value in user_info.items():
        profile[key] = value
    return profile


# retorno da função 
user_profile = build_profile('albert', 'einston', location='princeton', field='physic')

print(user_profile)