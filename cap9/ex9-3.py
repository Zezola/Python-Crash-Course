class User():
    def __init__(self, first_name, last_name, ocupation, age, city):
        ''' Initializing the attributes '''
        self.first_name = first_name
        self.last_name = last_name
        self.ocupation = ocupation
        self.age = age
        self.city = city
    

    def show_info(self):
        print("First name: " +self.first_name.title())
        print("Last name: " +self.last_name.title())
        print("Ocupation: " +self.ocupation)
        print("Age: " +str(self.age))
        print("City: " +self.city)
    

    def greet_user(self):
        print("Hello there "+self.first_name.title())


maria = User('maria', 'ribeiro', 'teacher', 24, 'lake city')
ricardo = User('ricardo', 'silva', 'mechanic', 30, 'niteroi')
clayton = User('clayton', 'meireles', 'broker', 45, 'sao paulo')

maria.show_info()
maria.greet_user()
print('\n')

ricardo.show_info()
ricardo.greet_user()
print('\n')

clayton.show_info()
clayton.greet_user()


