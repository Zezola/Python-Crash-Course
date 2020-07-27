class Carro():
    def __init__(self, make, model, year):
        ''' Initialize the attributes '''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 
    

    def read_odometer(self):
        ''' Print the odometer reading '''
        print("This car have " +self.odometer_reading+ " on it")
    
    def set_odometer_reading(self, miles):
        ''' Set the odometer_reading to an specific value '''
        self.odometer_reading = miles

    def increment_odometer_reading(self, miles):
        ''' Increment the odometer_reading by an specific value '''
        self.odometer_reading += miles
    
    def get_full_name(self):
        full_name = self.make + " " + self.model + " " +str(self.year)
        return full_name

class Bateria():
    ''' Uma bateria simples '''

    def __init__(self, tamanho_bateria = 70):
        ''' Inicializar os atributos '''
        self.tamanho_bateria = tamanho_bateria
    
    def descreve_bateria(self):
        ''' Imprime informaçoes sobre a bateria '''
        print("A bateria desse carro tem " +str(self.tamanho_bateria)+ "-kWh") 
    
    def get_max(self):
        if (self.tamanho_bateria == 70):
            maximo = 120
        elif (self.tamanho_bateria == 80):
            maximo = 130
        elif (self.tamanho_bateria == 85):
            maximo = 145
        
        msg = "O carro pode ir a " +str(maximo)+ " com a bateria cheia"
        print(msg)
    

    def upgrade_battery(self):
        if (self.tamanho_bateria != 85):
            print("atualizando bateria")
            self.tamanho_bateria = 85
        
      

    
class CarroEletrico(Carro):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.bateria = Bateria()

carro_eletrico = CarroEletrico('tesla', 'tesla x', 2030)
carro_eletrico.bateria.upgrade_battery()
print(carro_eletrico.get_full_name())
carro_eletrico.bateria.get_max()