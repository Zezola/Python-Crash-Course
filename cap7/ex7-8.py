'''
Make a list called sandwich_orders and fill it with the names of vari-
ous sandwiches. Then make an empty list called finished_sandwiches . Loop
through the list of sandwich orders and print a message for each order, such
as I made your tuna sandwich. As each sandwich is made, move it to the list
of finished sandwiches. After all the sandwiches have been made, print a
message listing each sandwich that was made.
'''

orders = ['x-tudo', 'x-bacon', 'x-duplo', 'cheddar', 'duplo cheddar', 'x-frango', 'x-peixe']

finished = []

while orders: 
    current_order = orders.pop()
    print("Fazendo o " +current_order)
    finished.append(current_order)

print("---- Todos sanduiches ------\n")
for sandwich in finished:
    print(sandwich)