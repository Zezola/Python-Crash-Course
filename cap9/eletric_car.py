from car import Car 


class Bateria():
    def __init__(self, tamanho = 70):
        self.tamanho = tamanho
    
    def describe(self):
        print("Temos uma bateria de " +str(self.tamanho)+ "kWh")
    
    def upgrade(self):
        if (self.tamanho < 85):
            print("Atualizando a bateria.")
            self.tamanho = 85


class CarroEletrico(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.bateria = Bateria()
