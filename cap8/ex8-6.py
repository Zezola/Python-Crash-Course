def city_name (city, country):
    info = "The city of " +city.title()+ " is in " +country.title()
    return info

santiago = city_name("Santiago", "Chile")
paris = city_name("Paris", "France")
tokio = city_name("Tokio", "Japao")

print(santiago)
print(paris)
print(tokio)