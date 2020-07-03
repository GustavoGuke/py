class Car():

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

        # rejeita alteracao caso tente passar um valor menor para o hodometro
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("YOU CAN´T ROLL BACK AN ODOMETER!")

    
    def increment_odomter(self, miles):
        """ soma a quantidade especificada ao valor de leitura do hodometro """
        
        # rejeita decrementacao, caso tente passar valores negativos.
        if miles < 0:
            print("YOU CAN´T ROLL BACK AN ODOMETER!")
        else:
            self.odometer_reading += miles


    def fill_gas(self):
        print('this car need a gas tank')



class EletricCar(Car):
    """ Representa aspectos de um carro especifico de  veiculos eletricos """

    def __init__(self, make, model, year):
        """ inicializa os atributos da classe pai. 
            Em seguida inicializa atributos especificos de um carro eletrico
        """

        # super cria uma conexoes entre a classe-pai e classe-filha
        super().__init__(make, model, year)

        # atributo especifico da classe EletricCar
        self.battery_size = 70
    
    def describe_battery(self):
        """ Exibe uma frase que descrve a capacidade da bateria """

        print(f'This car has a {self.battery_size} Kwh battery')    
    


    def fill_gas(self):
        """ sobrescreve o metodo da classe-pai que nao e utilizado na classe-filha """
        print("this car doesn´t need a gas tank")





# instanciando a classe filha
my_tesla = EletricCar('tesla', 'model s', 2016)

print(my_tesla.get_describe())
my_tesla.describe_battery()
my_tesla.fill_gas()

