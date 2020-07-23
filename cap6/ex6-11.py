cities = {
    "rio de janeiro": {
        "population": "2000",
        "country": "brazil",
        "fact": "police will kill you"
    },
    "sao paulo": {
        "population": "23023",
        "country": "brazil",
        "fact": "is big and dirty"
    },
    "belem": {
        "population": "2323",
        "country": "brazil",
        "fact": "is hot"
    }
}

for city, info in cities.items(): 
    print("\nNome: " +city)
    for item, value in info.items():
        print(item + ":" + value)