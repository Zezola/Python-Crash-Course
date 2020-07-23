guests = ['G1', 'G2', 'G3']

for i in range(0, 3):
    g = guests[i]
    print("Temos um convite para " +g)

wont_make_it = guests.pop(2)
new_guest = guests.insert(2, "New")

print(wont_make_it + " wont come")
print("New list\n")
for i in guests: 
    print("Please come to visit " +i)

print("I found a bigger table")

guests.insert(0, "teste1")
guests.insert(2, 'teste2')
guests.append('teste3')

for i in guests: 
    print("Hello "+i)

print("Sorry i can invite only 2 for dinner")

unvitted = guests.pop()
print("Sorry" +unvitted)
unvitted = guests.pop()
print("Sorry" +unvitted)
unvitted = guests.pop()
print("Sorry" +unvitted)
unvitted = guests.pop()
print("Sorry" +unvitted)

print("Ok, so the guests that will come are\n")
for i in guests:
    print(i)

del(guests[1])
del(guests[0])
print(guests)




