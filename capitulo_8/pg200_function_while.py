print('Devolvendo um Dicionário')

def greet(first_name, last_name):
    full_name = first_name +' '+ last_name
    return full_name.title()


while True:
    print('\nPlease tell me your name: ')
    print('(A qualquer momento entre com "q" para sair!)')
    f_name = input('First name: ')
    
    if f_name == 'q':
        break
    l_name = input('Last name: ')
    if l_name == 'q':
        break

    greet_formated = greet(f_name,l_name)
    print('\nHello ',greet_formated,'!')
    
