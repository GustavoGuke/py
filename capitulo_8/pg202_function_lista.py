print('Passando lista para uma função')

def user(names):
    for name in names:
        if name == 'gustavo':
            msg = 'Welcome, '+ name.title()
            print(msg)
        else:
            msg = 'Hello, '+name.title()
            print(msg)

'Passando a lista'
user_name = ['gustavo', 'Margor', 'Ty']



'função'
user(user_name)
