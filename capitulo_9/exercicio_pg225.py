import time

class Restaurant():
    """ Criar uma classe e instanciar ela 2 vezes """
    """ Exercicio 9.1 """

    def __init__(self,name, c_type):
        self.name = name
        self.c_type = c_type
        
    def open(self):
        print(f'{self.name.title()} ABERTO')


    def close(self):
        print('Fechando...')
        time.sleep(3)
        print('fechado\n')

# instanciando a classe
res_open = Restaurant('Pé de fava', 'cazeira')
# chamndo o metodos
res_open.open()
res_open.close()


res_close = Restaurant('Cogumelos', 'Nordestina')
print(f'Nome do Restaurante é {res_close.name} e sua culinaria é {res_close.c_type}')
res_close.close()



#============================================================================================================

class User():
    """ Exercicio 9.3 fazer uma classe de usuario atribuir dois metodos instanciar 2 vezes  """

    def __init__(self, first_name, last_name, **info ):
        """ variaveis de atributos """
        self.first_name = first_name
        self.last_name = last_name
        self.info = info
       

    def describe(self):
        show = {}

        show['first_name'] = self.first_name
        show['last_name'] = self.last_name

        if self.info:
            for k, v in self.info.items():
                show[k]=v
        return show
    

    def greet(self):
        print(f'Hello {self.first_name} {self.last_name}')




def show(dicionario):
    for chave, valor in dicionario.items():
        print(chave, valor)

    #print(dicionario)

# instanciando a classe user()
user_padrao = User('Gustavo','silva')
user_admin = User('Admin','admin', idade='50', city='sp')

# função para mostar as informações de usuarios
show(user_padrao.describe())

# mensagem de saudação de usuario
user_admin.greet()
show(user_admin.describe())
        