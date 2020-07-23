lista = ['bmw', 'audi', 'honda']

for i in lista:
    if (i == 'bmw'):
        print(i.upper())
    else:
        print(i.title())



sabores = ['mussarela', 'calabresa', '4queijos']

sabor_pedido = 'Mussarela'

if (sabor_pedido.lower() == 'mussarela'):
    print("Desculpe, houve um engano")
else:
    print("Bom apetite")




idades = [18, 17, 18, 21, 23, 27, 18, 17, 15, 14, 34, 28, 17, 18, 22, 21, 23, 20]

aprovados = []

for idade in idades:
    if (idade < 18) and (idade > 30 ):
        del idade

print(idades)
    
