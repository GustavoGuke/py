class car():

    def __init__(self, make, model, year ):
        """ inicializa os atributos que descrevem o carro """

        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0



    def get_describe(self):
        """ devolve um nome descritivo formatado de modo elegante """

        long_name =str(self.year) +' '+ self.model +' '+ self.make
        return long_name.title()


    def read_odometer(self):
        """ exibe uma frase que mostra as milhas do carro """

        print('miles ' + str(self.odometer_reading))


    # novo metodo para alterar um  atributo
    def update_odometer(self, mileage):
        """ define o valor de leitura do hodometro com o valor especificado """

        # rejeita alteração caso tente passar um valor menor para o hodometro
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("YOU CAN´T ROLL BACK AN ODOMETER!")

    
    def increment_odomter(self, miles):
        """ soma a quantidade especificada ao valor de leitura do hodometro """
        
        # rejeita decrementação, caso tente passar valores negativos.
        if miles < 0:
            print("YOU CAN´T ROLL BACK AN ODOMETER!")
        else:
            self.odometer_reading += miles







# instanciando a classe car
new_car = car('palio', 'weekend', 2004)
print(new_car.get_describe())




# alterando o valor de um atributo diretamente
# new_car.odometer_reading = 150




# alterando o valor do atributo  atraves de um novo metodo
new_car.update_odometer(150)





# incrementa valores na milhas 
new_car.increment_odomter(-1)
new_car.read_odometer()