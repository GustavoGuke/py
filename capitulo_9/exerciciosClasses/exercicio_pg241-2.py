class User():
    """ Exercicio 9.7 fazer uma subclasse Admin e mostar uma lista de privilegios """

    def __init__(self, first_name, last_name, **info ):
        """ variaveis de atributos """
        self.first_name = first_name
        self.last_name = last_name
        self.info = info
       

    def describe(self):
        """ Dicionario dos usuarios  """
        show = {}

        show['first_name'] = self.first_name
        show['last_name'] = self.last_name

        if self.info:
            for k, v in self.info.items():
                show[k]=v
        return show
    

    def greet(self):
        """ Saudação ao usuario """
        print(f'Hello {self.first_name} {self.last_name}')



    def show(self,show):
        """ Mostra o dicionario dos usuarios """
        for chave, valor in show.items():
            print(chave, valor)


class Admin(User):
    """ classe filha de User """

    def __init__(self, first_name, last_name, **info ):
        """ atributos classe pai """
        super().__init__(first_name, last_name, **info)

        self.privileges = ['can add post', 'can delete post', 'can ban user']


    def show_privileges(self):
        """ mostrar os privilegios do Adm """
        if self.first_name == 'admin':
            print(f'Your privileges:')

            for manager in self.privileges:
                print('\t',manager)
        else:
            print('Do you dont is admin')


root = Admin('estagiario','lira')

root.greet()
root.show_privileges()
