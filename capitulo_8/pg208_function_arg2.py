# Argumentos arbitrário

print('pizza.py')


def make_pizza(*toppings):
    """Exibe a lista de ingredientes pedidos"""
    for topping in toppings:
        print("-" + topping)
    
make_pizza('pepperoni')
make_pizza('extra cheese', 'calabreza')
print('...\n')



#argumentos posicionais e arbitrarios

print('pizza.py')

def make_pizzaMassa(massa,*toppings):
    print('Massa: '+massa)
    print('Toppings:')
    for i in toppings:
        print('\t-'+i)


""" entrada de dados do usuário
 massa = input('Qual a massa que vc gostaria: fina grosssa crocante: ') """
make_pizzaMassa('massa','calabreza','cheese extra','olive','catupiry')


