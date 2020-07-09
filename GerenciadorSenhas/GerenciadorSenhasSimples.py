import time

password_user = {}
senha_admin = '1'

autenticar =  input('Insira a sua senha master: ')
if autenticar != senha_admin:
    print('\nSenha invalida Encerrando!')
    print('\n')
    exit()


    
while True:
    print('\n')
    print('#'*30)
    print('#          Menu               #')
    print('#  0 : Sair                   #')
    print('#  1 : Inserir nova senha     #')
    print('#  2 : Listar serviços salvos #')
    print('#  3 : Apagar uma senha       #')
    print('#'*30,'\n')

    
    
    start = input('Escolha uma das opções do MENU: \n')

    if start == '0':
        print('Saindo...')
        time.sleep(2)
        break
 
    if start == '1':
        servico = input('Nome do serviço: ')
        senha = input('senha: ')
        password_user[servico] = senha
    #print(password_user, '\n')

    if start == '2':
        for keys, values in password_user.items():
            print('Serviço: ', keys)
            print('\tSenha: ', values)



    if start == '3':
         for keys, values in password_user.items():
            print('Serviço: ', keys)
         deletar = input('qual serviço deseja deletar: ')
         if deletar in password_user.keys():
            del password_user [deletar]
            

