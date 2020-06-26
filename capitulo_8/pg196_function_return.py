print('Exemplo Livro\n'
      'Devolvendo valores usando "return"')

def get_name( first_name, last_name):
    full_name = first_name +' '+last_name
    return full_name.title()

formated = get_name('gustavo','lima')
print(formated)
print('...\n')

#==============================================================================

print('Deixando um argumento opcional')

def get_formated(first_name, last_name, middle_name=''):
    
    if middle_name:
        full_name = first_name +' '+ last_name +' '+ middle_name
    else:
        full_name = first_name +' '+last_name
    return full_name.title()

formatedd = get_formated('gustavo','silva')
print(formatedd)
print('...\n')

#==============================================================================
        
