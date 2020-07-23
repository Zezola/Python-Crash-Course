fav_numbers = {
    "mark": [1, 2, 4],
    "julia": [2, 4, 0],
    "dan": [12, 23],
    "gilbert": [8, 9, 7]
}

for person, numbers in fav_numbers.items():
    print("\n" +person+"\'s fav numbers are:")
    for number in numbers:
        print(number)
