import time
import sqlite3


senha_admin = '1'
autenticar =  input('Inserir senha master: ')


if autenticar != senha_admin:
    print('\nSenha invalida Encerrando!')
    print('\n')
    exit()



class Bd():
    """ banco de dados """

    def __init__ (self):
        """ iniciar os atributos e criar a estrutura do  banco de dados """
        self.service = ''
        self.password = ''
        self.conn = sqlite3.connect('password.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS senhas(
                services TEXT NOT NULL,
                passwords TEXT NOT NULL
                );
                ''')


    def insert_password(self, service, password):
        """ inserir dados no banco """
        self.service += service
        self.password += password
        self.cursor.execute(f'''
            INSERT INTO senhas (services, passwords)

            VALUES ('{self.service}', '{self.password}')
            ''')
        self.conn.commit()


    def show_services(self):
        """ visualizar os dados  """
        for row in   self.cursor.execute(''' SELECT * FROM senhas;'''):
            print(row)


    def delete_password(self):
        """ deletar o dados """
        for row in self.cursor.execute(''' SELECT * FROM senhas;'''):
            print(row)

        deletar = input('Escolha um serviço que queira deletar: ')
        sql = (f''' DELETE FROM senhas WHERE services = '{deletar}' ''') 
        self.cursor.execute(sql)
        self.conn.commit()


      
# intanciando a classe
my_db = Bd()

# onde a magica acontece
while True:
    print('\n')
    print('#'*31)
    print('#          Menu               #')
    print('#  0 : Sair                   #')
    print('#  1 : Inserir nova senha     #')
    print('#  2 : Listar serviços salvos #')
    print('#  3 : Apagar uma senha       #')
    print('#                             #')
    print('#'*31,'\n')


    start = input('Escolha uma das opções do MENU: \n')


    if start == '0':
        print('\n')
        print('#'*31)
        print('#          Menu               #')
        print('#  0 : Sair                   #')
        print('#                             #')
        print('#'*31,'\n')
        print('Saindo...')
        
        time.sleep(2)
        break
 

    if start == '1':
        print('\n')
        print('#'*31)
        print('#          Menu               #')
        print('#  1 : Inserir nova senha     #')
        print('#                             #')
        print('#'*31,'\n')

        servico = input('Nome do serviço: ')
        senha = input('senha: ')
        my_db.insert_password(servico, senha)
  

    if start == '2':
        print('\n')
        print('#'*31)
        print('#          Menu               #')
        print('#  2 : Listar serviços salvos #')
        print('#                             #')
        print('#'*31,'\n')

        my_db.show_services()
    

    if start == '3':
        print('\n')
        print('#'*31)
        print('#          Menu               #')
        print('#  3 : Apagar uma senha       #')
        print('#                             #')
        print('#'*31,'\n')

        my_db.delete_password()
    

