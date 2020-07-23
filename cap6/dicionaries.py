# Nesse capitulo iremos aprender a usar dicionarios em Python
# que nos permitem conectar pedaços de informação que estão relacionados 
# Como dicionarios nos permitem guardar um numero quase infinito de informação 
# Vamos aprender como modificar essas informações, passar por elas com um loop, 
# Guardar dicionarios dentro de listas e listas dentro de dicionarios e até dicionarios
# dentro de outros dicionarios. 
# Com dicionarios podemos criar modelos pra uma variedade de objetos que existem no mundo
# real, como pessoas, carros, casas, animais, montanhas, e etc. 

# Vamos supor que queremos criar um dicionario pra guardar algumas informaçoes 
# sobre um alien que temos em um jogo de aliens. 

alien_0 = { 'color': 'green', 'points': 5}
alien_1 = { 'color':'blue', 'points': 5}

print("Alien color "+alien_0['color'])
print("Alien points " +str(alien_0['points']))

# Como dicionarios sao estruturas dinamicas, podemos adicionar ou remover pares chaves-valor 

pessoa = {
    "nome" : "Ana Silva Sauro"
}

pessoa["idade"] = 20
print(pessoa)

# As vezes é necessário e conveniente começarmos com um dicionario vazio 
# e adicionarmos valores a ele a medida que vamos precisando 

carro = {}

carro["cor"] = "prata"
carro["fabricante"] = "honda"
carro["modelo"] = "civic"
carro["ano"] = 2010

# Geralmente fazemos isso quando estamos trabalhando com dados fornecidos pelo usuario
# Podemos mudar o valor de alguma chave, por exemplo, cor. Acessamos normalmente, e definimos
# o novo valor

carro["cor"] = "branco"

# Podemos remover também um valor usando o comando del e acessando o par chave-valor que precisamos

del carro["ano"]


