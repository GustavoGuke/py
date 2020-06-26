# importando modulos / 
# Podemos ultilizar um alias nas chamadas  
# import pizza as p =  importo o mudulo todo
# from pizza import make_pizza as mp =  importo apenas a função especifica
# import pizza * =  desse modo ele importa tds as funçoes do modulo especificado


# fazendo import do modulo pizza.py que tem uma função make_pizza
'''
import pizza

pizza.make_pizza(16, 'extracheesse')
pizza.make_pizza(8, 'calabreza', 'olive', 'onion')
'''

# importando funções especificas / importando apenas funções que eu queira de outro modulo

from pizza import make_pizza

make_pizza(10, 'mussarela')



