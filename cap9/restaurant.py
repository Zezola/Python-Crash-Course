class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
    
    def show_info(self):
        print("The restaurant "+self.name+ " works with " +self.cuisine_type+ " cuisine")