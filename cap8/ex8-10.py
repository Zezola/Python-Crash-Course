def print_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians, great):
    while magicians:
        magician = magicians.pop()
        great.append(magician)
    
def show_magicians(great):
    for magician in great:
        print("The great " +magician)

magicians = ['Zatanna', 'Constantine', 'Dr Destiny']
great = []

print_magicians(magicians)
make_great(magicians, great)
show_magicians(great)