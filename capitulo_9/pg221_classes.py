class Dog():
    """ Primeiro programa usando classe simples  *modelar cachorro* """
    """ Funções dentro de classe sao chamadas de metodos """

    def __init__(self, name, age):
        """ Inicializar os atributos name e age """
        self.name = name
        self.age = age
    
    def sit(self):
        """ Simula uma cachorro sentando em resposta a um comando """

        print(f'{self.name.title()} is now sitting. ')

    def roll_over(self):
        """ Simula um cachorro rolando em resposta a um comando """

        print(f'{self.name.title()} rolled over.\n')

# instânciando a classe
my_dog = Dog('duque', 10)

# acessando os atributos
print(f'\n Nome {my_dog.name} idade {my_dog.age}')

# chamando o metodos
my_dog.sit()
my_dog.roll_over()



# segunda instancia da classe Dog()
your_dog = Dog('bob', 2)
print(f'Nome {your_dog.name} idade {your_dog.age}')
your_dog.sit()
your_dog.roll_over()



# função para trazer um novo dog instanciando a classe 
def chama(classe):
    print(f'Nome {classe.name} idade {classe.age}')
    classe.sit()
    classe.roll_over()

classe = Dog('dino',1)
chama(classe)

