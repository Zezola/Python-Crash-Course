requested_toppings = ['mushrooms', 'onions', 'extra cheese']

for topping in requested_toppings:
    print("Adding " +topping+ " to your pizza")

print('Here\'s your pizza')

''' Mas e se ficarmos sem um desses toppings? Vamos supor que estamos sem mushrooms ''' 


for topping in requested_toppings:
    if (topping.lower() == 'mushrooms'):
        print('Sorry we\'re out of mushrooms')
    else:
        print('Adding ' +topping+ ' to your pizza')


''' E se a nossa lista estiver vazia? Vamos fazer essa verificao no exemplo abaixo '''
requested_toppings = []

if requested_toppings:
    for topping in requested_toppings:
        print("Adding " +topping+ " to your pizza")
else:
    print("Are you sure you want a plain pizza?")

''' Podemos trabalhar tambem com mais de uma lista ao mesmo tempo ''' 

available_topics = ['mushrooms', 'chicken', 'extre cheese', 'peperoni', 'pineaple', 'olives']

requested_toppings = ['mushrooms', 'fries', 'olives']

for requested_topping in requested_toppings:
    if requested_topping in available_topics:
        print("Adding " +requested_topping+ " to your pizza")
    else:
        print("Sorry, we dont have " +requested_topping)

print("Heres your pizza")