print('Devolvendo um Dicionário')

def data_person(first_name, last_name, age =''):

    'Construção do dicionário'
    person = {'first': first_name, 'last': last_name}

    'age é opcional, caso nao seja passado nenhum dado age aparece'
    if age:
        person['age']= age
    return person

data = data_person('Gustavo','Silva')

print(data)
    
