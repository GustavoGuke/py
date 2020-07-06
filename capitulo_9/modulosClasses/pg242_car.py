class Car():
    """ classe para representar um carro """

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






class Battery():
    """ tentativa simples de modelar uma bateria """

    def __init__(self, battery_size=70):
        """ inicializa atributos da bateria """
        self.battery_size = battery_size

    def describe_battery(self):
        """ Exibe uma frase que descrve a capacidade da bateria """

        print(f'This car has a {self.battery_size} -Kwh battery') 
    

    def get_range(self):
        """ exibe uma frase sobre a distancia que o carro e capaz de percorrer com essa bateria """

        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 80:
            range = 270

        message = 'this car can go approximately '+str(range)
        message += 'miles on a full charge. '
        print(message)





class EletricCar(Car):
    """ Representa aspectos de um carro especifico de  veiculos eletricos """

    def __init__(self, make, model, year):
        """ inicializa os atributos da classe pai. 
            Em seguida inicializa atributos especificos de um carro eletrico
        """

        # super cria uma conexoes entre a classe-pai e classe-filha
        super().__init__(make, model, year)

        # instancia como atributos
        self.battery_size = Battery()
    
    def fill_gas(self):
        """ sobrescreve o metodo da classe-pai que nao e utilizado na classe-filha """
        print("this car doesn´t need a gas tank")