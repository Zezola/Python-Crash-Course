msg = "Digite sua idade e vamos dizer quanto custa seu ingresso\n"
msg += "Pra sair digite quit"

active = True

age = input(msg)

while active:
    if (int(age) < 3):
        print("Seu ingresso e gratuito")
        age = input(msg)
    elif (int(age) >= 3 and int(age) < 12):
        print("Seu ingresso custa R$10")
        age = input(msg)
    elif (int(age) >= 12):
        print("Seu ingresso custa R$15")
        age = input(msg)
    elif (age == 'quit'):
        active = False
    