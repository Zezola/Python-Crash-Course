class Restaurant():
    def __init__(self, name, cuisine_type):
        ''' Initiating the variables '''
        self.name = name
        self.cuisine_type = cuisine_type
    
    
    def describe(self):
        print("Welcome to " +self.name)
        print("The best " +self.cuisine_type+ " cuisine on the region")
    

    def open(self):
        ''' Print a message saying that the restaurant is open '''
        print(self.name + " is now open")


leos = Restaurant("Leos", "Italian")
roses = Restaurant("Roses", "Brazilian")
churrascaria = Restaurant("Churrasco", "Churrasco")

leos.describe()
leos.open()
roses.describe()
roses.open()
churrascaria.describe()
churrascaria.open()



