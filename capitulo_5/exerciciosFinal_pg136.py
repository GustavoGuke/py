#EXERCICIO 1===============================================================
#MENSAGEM PARA USUÁRIOS, MSG DIFERENTE PARA O ADMIN

usuarios = ['admin','frontEnd','backEnd', 'fullStack']

for i in usuarios:
    if i == 'admin':
        print('Ola admin seja bem vindo ')
    else:
        print('Seja bem vindo novamente '+ i)


#EXERCICIO 2=================================================================
print('\n\n')
#MENSAGEM PARA USUARIOS, SE NAO TIVER USUARIOS IRA PARA O ELSE
usuarios1 = []

if usuarios1:
    for i in usuarios1:
        if i == 'admin':
            print('Ola admin seja bem vindo ')
        if i != 'admin':
            print('Seja bem vindo novamente '+ i)
else:
    
    print('Temos que contratar')


#EXERCICIO 3=================================================================
    
print('\n\n')
#VERIFICANDO NOMES DE USUARIOS
user_antigos = ['Gustavo','Gabriel','Joao','Lorena']
user_novos = ['LORENA','Joao','betina','paulo']


for i in user_novos:
    i = i.title()
    if i in user_antigos:
        print('nome ja existe, favor alterar ', i)
    if i not in user_antigos:
        user_antigos.append(i)
        print('Nomes adicionados ',i)
print(user_antigos)




#EXERCICIO 4=================================================================
print('\n\n')
#NUMEROS ORDINAIS 

num_ordinais = [1,2,3,4,5,6,7,8,9]

for i in num_ordinais:
    if i == 1:
        print(i,'st')
        
    elif i == 2:
        print(i,'nd')
        
    elif i == 3:
        print(i,'rd')
        
    else:
        print(i,'th')






