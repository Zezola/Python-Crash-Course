def make_great(magicians, great):
    magicians_copy = magicians[:]
    while magicians_copy:
        mag = magicians_copy.pop()
        great.append(mag)
    return great

def show_magicians(magicians, great):
    print("Original List: \n")
    for magician in magicians:
        print(magician)
    print('\n')
    print("Great magicians\n")
    for great_mag in great:
        print("the great "+great_mag)

magicians = ['Zatanna', 'Constantine', 'Midnight']
great = []

make_great(magicians, great)
show_magicians(magicians, great)