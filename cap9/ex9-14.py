from random import randint

class Dice():
    ''' Modeling a dice with the standart value of sides = 6 '''
    def __init__(self, sides = 6):
        self.sides = sides
    
    def roll(self):
        value = randint(1,self.sides)
        return value

d6 = Dice()
print(d6.roll())
print(d6.roll())
print(d6.roll())
print(d6.roll())
print(d6.roll())
print(d6.roll())

# Making a d20 
print("D20 rolls:")
d20 = Dice(20)
print(d20.roll())
print(d20.roll())
print(d20.roll())
print(d20.roll())
print(d20.roll())
print(d20.roll())
print(d20.roll())
print(d20.roll())
print(d20.roll())
print(d20.roll())
print(d20.roll())

# Making a d10
print("D10 rolls:")
d10 = Dice(10)
print(d10.roll())
print(d10.roll())
print(d10.roll())
print(d10.roll())
print(d10.roll())
print(d10.roll())

