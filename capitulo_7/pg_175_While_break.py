print('Laço while usando break')

lista_de_lugares = []
ativo = True
while ativo:
    lugares = input('Digite lugares onde gostaria de visitar: ')
    lista_de_lugares.append(lugares)

    if lugares == 'sair':
        ativo = False
    else:
        print(lista_de_lugares)

#=============================================================================

lista_de_aprendizado = []

active = True
while active:
    stacks = input('Digite as linguagens que esta estudando: ')
    lista_de_aprendizado.append(stacks)

    if stacks == 'go':
        print('MENTIROSO')
        break
    
    elif stacks == 'sair':
        active = False
    else:
        print(lista_de_aprendizado)
print('\n\n')
#==============================================================================

print('Comando continue')

cont = 0

while cont < 10:
    cont = cont + 1
    if cont % 2 == 1:
        continue
    print(cont)

#===================================== ate pg177 ==============================























