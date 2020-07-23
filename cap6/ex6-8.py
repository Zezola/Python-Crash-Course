pet1 = {
    "animal" : "dog",
    "owner" : "Mark",
    "name" : "Zeus"
}

pet2 = {
    "animal": "bird",
    "owner": "Zana",
    "name": "Pidgeot"
}

pet3 = {
    "animal": "mouse",
    "owner": "Daniel",
    "name": "Ratatouile"
}

pets = [pet1, pet2, pet3]

for pet in pets:
    name = pet["name"]
    kind = pet["animal"]
    owner = pet["owner"]
    print("The pet is a " +kind+ " called " +name+ " owned by " +owner)