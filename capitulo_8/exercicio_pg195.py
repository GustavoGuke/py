print('Exercicio 8.3')
print('Escreva uma função que aceite dois argumentos, chame ela duas vezes \n'
      'usando argumentos posicionais e argumentos nomeados!\n')


def make_shirt(size,text):
    print(f'Tamanho {size} eo texto na estampa é {text}')
make_shirt('M','Hello Word')
make_shirt(text='condig<>',size='P')    
print('...\n')




def make_shirt_big(text='I love Python',size='G'):
    print(f'Tamanho {size}, texto {text}')
make_shirt_big()
make_shirt_big(size='M')
make_shirt_big(text='Function')
print('...\n')




def describe_city(city='São Paulo',country='Brasil'):
    print(f'Cidade: {city} localizada no:  {country}')
describe_city()
describe_city(city='Tóquio',country='Japão')
describe_city(city='Rio de Janeiro')
