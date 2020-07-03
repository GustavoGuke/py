class Restaurant():
    """ Criar uma classe pegando a do exercicio 9.4 como referencia """
    """ Exercicio 9.6 """

    def __init__(self,name, c_type):
        self.name = name
        self.c_type = c_type
        self.number_served = 0
        

    def open_restaurant(self):
        """ frase para dizer que o restaurante esta aberto """
        print(f'{self.name.title()} ABERTO')


    def client_number(self, number):
        """ mostra o numero de clientes atendidos no restaurante """
        self.number_served += number
        print(self.number_served, 'Clientes')


    def increment_client(self, cliente):
        """incrementar ou decrementar clientes no restaurante """

        if cliente < 0:
            self.number_served += cliente
            print(f'Clientes acabaram de sair {str(cliente)}, temos vagas!')
            print(f'Agora temos {self.number_served} no restaurante')
        else:
            self.number_served += cliente
            print(f'Clientes sendo atendidos {str(self.number_served)}')
        

    def close(self):
        """ frase para dizer que o restaurante esta fechado """
        print(f'{self.name.title()} FECHADO!\n')






class IceCreamStand(Restaurant):
    """ classe- filha de Restaurant """
    
    def __init__(self, name, c_type):
        """ inicializa os atributos da classe pai """

        super().__init__(name, c_type)

        self.flavors = ['morango', 'milho', 'chocolate', 'flocos']


    def show_flavors(self):
        """ itera sobre a lista de sabores de sorvetes """

        print(' Sorveteria\n Sabores:')
        for i in self.flavors:
            print(f'\t{i}')



# instancia a classe filha
sorvetes = IceCreamStand('Cogumelo', 'caseira')

# metodo classe pai
sorvetes.open_restaurant()

# metodo classe pai
sorvetes.client_number(5)

# metodo classe filha
sorvetes.show_flavors()

# metodo classe pai
sorvetes.increment_client(-2)

'''
restaurante.increment_client(-2)

restaurante.close()
'''
#==========================================================================================================
