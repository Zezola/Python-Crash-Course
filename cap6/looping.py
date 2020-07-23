# Um dicionario pode conter algumas informaçoes ou milhoes. 
# Como tem um numero ilimitado do que podemos guardar em um dicionario
# Python nos deixa acessar seus valores usando um loop 

# Loop por todos pares chave-valor 

user_0 = {
    "username": "Nami",
    "first": "Namioka",
    "last": "Shinju"
}

# Podemos usar um loop pra acessar todos esses valores 

for chave,valor in user_0.items():
    print("\nKey :" +chave)
    print("Value :" +valor)

# Aqui usamos o metodo items() que retorna os pares chave-valor de um determinado dicionario
# Essa abordagem funciona particularmente bem quando estamos acessando dicionarios onde 
# guardamos o mesmo tipo de informaçao pra diferentes chaves 

fav_languages = {
    "jen": "python",
    "carla": "C",
    "rico": "java"
}

for nome, linguagem in fav_languages.items():
    print("Nome "+nome)
    print("Language "+linguagem)


# Indo por todas as CHAVES em um dicionario 
# Metodo util quando nao precisamos de todos os valores no dicionario 

fav_pizzas = {
    "jen": "mussarela",
    "carla": "pepperoni",
    "paulo": "anchoves",
}

for name in fav_pizzas.keys():
    print(name)

# Na verdade fazer o loop pelas chaves é o comportamento padrão quando trabalhamos com dicionarios
# Entao o codigo abaixo ia resultar na mesma coisa: 

for name in fav_pizzas:
    print(name)

# Voce pode acessar qualquer chave que você quiser dentro do dicionario. Vamos
# printar uma mensagem caso um dos nomes do dicionario bata com o nome da lista
# de amigos 

amigos = ['jen', 'carla']

for name in fav_pizzas:
    print(name.title())

    if name in amigos:
        print("Hi " +name+ " nice to see that you like " +fav_pizzas[name])

# Podemos usar o keys() pra ver se uma chave especifica esta em nosso dicionario

if "erin" not in fav_pizzas.keys():
    print("Please erin take your poll")

# Fazendo o loop em ordem :
# Um dicionario sempre mantem uma correspondencia entre uma chave e o valor que está 
# associado a ela, mas você não consegue os items em uma ordem especifica. 
# Caso queiramos, podemos ordenar os items a medida que eles sairem do loop for 
# Utilizando o metodo sorted() 
for name in sorted(fav_pizzas.keys()):
    print(name.title() + ", thank you")

# Looping por todos valores no dicionario 
# As vezes so estamos interessados nos valores que o dicionario tem. 
# Entao podemos usar o metodo values() 

fav_languages = {
    "jen": "C",
    "pedro": "Ruby",
    "janaina": "Scala",
    "lucas": "Python",
    "peter": "Python",
    "Max": "C",
    "matheus": "Python"
}

print("As linguagems que foram mencionadas: ")
for language in fav_languages.values():
    print(language.title())

# Essa abordagem pega todos valores do dicionario sem checar por repetiçao
# em alguns casos não vamos querer esse comportamento. Entao podemos usar o metodo set() 
# o metodo set() é parecido com uma lista, mas ele não admite repetição de items 

print("As linguagens mencionadas foram: ")
for linguagem in set(fav_languages.values()):
    print(linguagem)

