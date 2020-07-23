def print_models(unprinted, printed):
    while unprinted:
        model = unprinted.pop()
        print("Printing " +model)
        printed.append(model)


def show_models(printed):
    print("The printed models:")
    for model in printed:
        print(model)