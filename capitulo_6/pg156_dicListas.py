print('uma lista de dicionário')
alien_0 = {'color':'green', 'points':5}
alien_1 = {'color':'yellow', 'points':10}
alien_2 = {'color':'red', 'points':15}

aliens = [alien_0, alien_1, alien_2]
for i in aliens:
    print(i)
print('...')
#=============================================================================

#criar uma lista para armazenar aliens
l_alien = []

# cria 10 aliens verdes
for alien_num in range(10):
    new_alien = {'color':'green', 'points':5}
    l_alien.append(new_alien)

#mostra os 5 primeiros aliens criados
for mostrar in l_alien[:5]:
    print(mostrar)
print('...')
print('total de aliens criados', str(len(l_alien)))

#=============================================================================
print('...')
print('mudando a cor dos aliens')
for mudar in l_alien[0:3]:
    if mudar['color']=='green':
        mudar['color']='red'
        mudar['points']=15
for mudar in l_alien[3:6]:
    if mudar ['color']=='green':
        mudar['color']='yellow'
        mudar['points']=10
    
for i in l_alien[0:9]:
    print(i)
#============================== até pg159 ====================================
#   ===========================================================================

