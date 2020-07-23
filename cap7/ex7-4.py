msg = "\nInput the toppings that you wanna for your pizza. When you're done enter quit\n"

toppings = input(msg)

while toppings != 'quit':
    print("We'll add " +toppings+ " to your pizza")
    toppings = input(msg)
