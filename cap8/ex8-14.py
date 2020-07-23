def make_car(manufacturer, model, **info):
    # Fazer o dicionario 
    car = {}
    # Passar os argumentos obrigatórios
    car['manufacturer'] = manufacturer
    car['model'] = model
    # Passar os arbitrarios
    for chave, valor in info.items():
        car[chave] = valor
    # Retornar o dicionario
    return car

def show_car(car):
    for chave, valor in car.items():
        print(chave+ " = "+valor )

honda = make_car('Honda', 'Civic', transmissao = "manual", motor = "2.0li")
show_car(honda)