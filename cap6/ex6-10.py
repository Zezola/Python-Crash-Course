fav_places = {
    "mark": ["Home", "Work", "Market"],
    "julia": ["Park", "Forest", "City"],
    "ana": ["Bar", "Street", "Desert"]
}

for person, places in fav_places.items():
    print("\nThe fav places of " +person)
    for place in places:
        print(place)