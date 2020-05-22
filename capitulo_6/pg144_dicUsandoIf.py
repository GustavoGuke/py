print('*******************************\n'
      'Programa de Velocidade do Alien\n'
      '*******************************')

alien = {'x_position':0, 'y_position':25, 'speed':'slow'}
print('Original x-position: ' + str(alien['x_position']))

if alien['speed'] == 'slow':
    x_increment = 1
elif  alien['speed'] == 'medium':
    x_increment = 2
else:
     x_increment = 3

alien['x_position'] = alien['x_position'] + x_increment
print('New x-position: ' + str(alien['x_position']))

print('\n\n')
#==============================================================================

print('Removendo pares chave-valor')
dados = {'nome':'Gustavo', 'idade':30}
print(dados)

del dados['idade']
print(dados)
print('\n\n')
#==============================================================================

stack = {
     'Academy':'Python',
     'Udemy':'HTML',
     'Innovation':'Angular',
     'Youtube':'JavaScript'
      }
print(stack)
#================================= pag 147 ====================================
#===============================================================================
