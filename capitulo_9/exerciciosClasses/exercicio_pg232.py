class Restaurant():
    """ Criar uma classe pegando a do exercicio 9.1 como referencia """
    """ Exercicio 9.4 """

    def __init__(self,name, c_type):
        self.name = name
        self.c_type = c_type
        self.number_served = 0
        

    def open(self):
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


restaurante = Restaurant('cogumelo', 'caseira')
restaurante.open()
restaurante.client_number(10)

restaurante.increment_client(-2)

'''


restaurante.close()
'''
#==========================================================================================================
