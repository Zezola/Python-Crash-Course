fav_languages = {
    'tim': "C",
    'monica': "Python",
    'chandler': "Scala"
}

guests = ['barney', 'tim', 'ross', 'monica', 'cebolinha', 'cascao']

for guest in guests:
    if guest in fav_languages.keys():
        print(guest +" thanks for taking the poll")
    else:
        print(guest +" please take the poll")
