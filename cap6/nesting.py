# As vzes queremos guardar uma lista de dicionarios, ou um lista dentro de um dicionario
# Isso se chama aninhamento, e temos algumas formas de faze-los. 

# Uma lista de dicionarios 
pessoa1 = { "nome": "Bira", "idade":"20"}
pessoa2 = { "nome": "Gabriel", "idade": "20"}
pessoa3 = { "nome": "Pedro", "idade": "30"}

pessoas = [pessoa1, pessoa2, pessoa3]

for pessoa in pessoas:
    print(pessoa)

# Podemos criar uma lista de objetos iguais dessa forma

canetas = []

for i in range(30):
    canetas.append({"marca":"bic", "cor":"azul"})

for caneta in canetas:
    print(caneta)

# Apesar de todos objetos serem iguais, cada um é um objeto separado. 
# o que nos permite modificar caso precisemos. Por exemplo, se houve um engano
# e queremos trocar a cor das 5 primeiras canetas pra preto. 

for caneta in canetas[0:5]:
    if caneta["cor"] == 'azul':
        caneta["cor"] = 'preto'

for i in range(5):
    print(canetas[i])


# Listas dentro de dicionarios tambem podem ser uteis. Por exemplo

pizza = {
    'borda':'sem-recheio',
    'sabores': ['mussarela', 'calabresa', 'presunto']
}

print("Sua borda " +pizza["borda"]+ " e o sabor da sua pizza e " +pizza["sabores"][2])

# Podemos usar outro loop for pra percorrer os elementos da lista que esta dentro do dicionario

fav_languages = {
    "jen": ["Scala", "Go"],
    "rob": ["Python", "Javascript"],
    "dan": ["Java", "Ruby"]
}

for name, languages in fav_languages.items():
    print("\n" + name.title() + " your favourite languages are: ")
    for language in languages: 
        print("\t" +language)

# Dicionarios dentro de dicionarios 
# Podemos botar dicionarios dentro de dicionarios. O contra é que o nosso codigo pode ficar
# mais complicado se sairmos fazendo isso sem cuidado 

users = {
   "pedroca": {
       "name": "pedro",
       "email": "pedro@mail.com"
   },
   "juliann":{
       "name": "anna julia",
       "email": "juliana@mail.com"
   }
}

for username, info in users.items():
    print("\n Username " + username)
    name = info["name"]
    email = info["email"]
    print("\t Name : " +name)
    print("\t Email: " +email )

