def make_pizza(size,*toppings):
    """ Apresentar a pizza que vamos montar """
    print('\n Making a ' + str(size) +
        '-inch  pizza with the following toppings: ')
    for topping in toppings:
        print('-' + topping)