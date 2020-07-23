def make_sandwich(*items):
    for item in items:
        print("Adding "+item+" to your sandwich")
    print("Sandwich ready")

make_sandwich('peperonni', 'cheese', 'ketchup')
make_sandwich('meatballs', 'cheese')
make_sandwich('onions')