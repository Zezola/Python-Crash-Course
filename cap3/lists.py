# Uma lista guarda uma coleção de dados 

pessoas = ["Ana", "Paulo", "Lucia"]
print(pessoas[0])
print(pessoas[1])
print(pessoas[2])

msg = "Boa noite"

print(msg + " " + pessoas[0])
print(msg + " " + pessoas[1])
print(msg + " " + pessoas[2])

musicas = ["Vampires", "Midnight City", "Shadows"]

artistas = ["The Midnight", "M83", "The Midnight"]

print("A musica " + " " +musicas[0]+ " e do artista " + artistas[0])
print("A musica " + " " +musicas[1]+ " e do artista " + artistas[1])
print("A musica " + " " +musicas[2]+ " e do artista " + artistas[2])

# If want to modify some element in my list, i can do it by accessing his index 
compras = ["Limao", "Uva", "Laranja"]

compras[0] = "Ovos"

print(compras)

# Sometimes we want to add new elements to a list of items. Python provides us some ways to do it
# we can append it to the end of the list using list.append('new_item')

compras.append("Leite")
print(compras)

# We can add elements in a determined position using list.insert(position, item)

compras.insert(2, 'Pao')
print(compras)

# And, we can remove items too. If you know his position, we can use the del statement 
del compras[2]
print(compras)

# And we can use the pop() method too. The difference is that the pop method allows us to
# access that value later. 

item = compras.pop() 
print(item)
print(compras)

# The element was taken from the list but we still used its value 
# we can do it with any os our elements, we just need to know the position 

item = compras.pop(1)
print(compras)
print(item)

# Now we specified that we wanted the element of index 1, and used his value in the 
# item variable 
# Sometimes we dont know the position of a value. We can remove this value with the 
# remove() method

compras.remove("Ovos")
print(compras)