''' Cria um modelo simples pra um carro '''

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def get_fullname(self):
        full_name = self.make + " " +self.model + " " +str(self.year)
        return full_name

