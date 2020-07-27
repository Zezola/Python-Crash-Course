class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
    
    def show_info(self):
        print("The restaurant "+self.name+ " works with " +self.cuisine_type+ " cuisine")
    

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavours = ['chocolate', 'strawberry', 'vanilla']
    
    def show_flavours(self):
        for flavour in self.flavours:
            print(flavour)

ice_cream = IceCreamStand("Jose", "ice cream")
ice_cream.show_info()
ice_cream.show_flavours()