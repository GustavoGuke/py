print('\nExercicio 8.12')
# função deve receber uma lista de sanduiches e ser mostrada 3 vezes

def make_lista(*lista):
    pedido = []

    for i in lista:
        pedido.append(i)
    print(pedido)

make_lista('x-tudo')
make_lista('x-bacon','x-clabreza','x-egg')
make_lista('x-salada','fritas')
print('...\n')

# função deve receber um dicionario contendo perfil de uma pessoa

def user_profile(**profile):
    profile_user = {}

    for k, v in profile.items():
        profile_user[k]=v
    print(profile_user)

user_profile(nome='Gustavo',sobreNome='silva',idade='25')
user_profile(nome='Gabriel',sobreNome='lima', idade='6')
print('...\n')


# função deve receber um dicionario nomeado e arbitrario contendo informações de um carro

def make_car(name, company, **info):
    car = {}
    car['name']=name
    car['company']=company

    for key, value in info.items():
        car[key]=value
    return car

def show(cars):
    for k, v in cars.items():
        print(k,':',v)

cars = make_car('palio wekeend', 'fiat', year='2005', color='ciano')

print(cars)
show(cars)