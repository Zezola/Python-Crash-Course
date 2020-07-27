class Restaurant():
    def __init__(self, name, cuisine_type):
        ''' Init the attributes values '''
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    

    def set_number_served(self, number):
        ''' Change the value of the attribute number_served '''
        self.number_served = number
    
    def increment_number_served(self, number):
        ''' Increment the number of served customers '''
        self.number_served += number

    def get_info(self):
        ''' Prints info about the restaurant '''
        print("Name: " +self.name)
        print("Cuisine type: " +self.cuisine_type)
        print("Number served: " +str(self.number_served))
    
    def open(self):
        ''' Print that the restaurant is open '''
        print("We're open : " +self.name)

    def closed(self):
        ''' Print if the restaurant is closed '''
        print(self.name + " is closed")



leos = Restaurant('Leos', 'Italian')
leos.number_served = 20
leos.increment_number_served(10)
leos.get_info()


    
