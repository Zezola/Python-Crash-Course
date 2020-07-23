'''
Using the list sandwich_orders from Exercise 7-8, make sure
the sandwich 'pastrami' appears in the list at least three times. Add code
near the beginning of your program to print a message saying the deli has
run out of pastrami, and then use a while loop to remove all occurrences of
'pastrami' from sandwich_orders . Make sure no pastrami sandwiches end up
in finished_sandwiches .
'''

sanduiches = ['x-tudo', 'pastrami', 'x-bacon', 'pastrami', 'x-egg', 'pastrami', 'x-junior']

finished = []

print("Ops, acabou o pastrami\n")

while 'pastrami' in sanduiches:
    sanduiches.remove('pastrami')

while sanduiches:
    fazendo = sanduiches.pop()
    print("Fazendo o " +fazendo)
    finished.append(fazendo)

print("---Todos sanduiches----\n")
for sanduiche in finished:
    print(sanduiche)