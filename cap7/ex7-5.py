age = int(input("Digite a sua idade"))

while True:
    if (age < 0):
        print("Idade invalida. Digite uma idade valida:\n")
        age = int(input("Digite sua idade"))
    elif (age <= 3):
        print("Seu ingresso e gratuito")
        break 
    elif (age > 3 and age <= 12):
        print("Seu ingresso custa R$10")
        break
    else:
        print("Seu ingresso custa R$15")
        break


