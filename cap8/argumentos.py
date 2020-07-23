# Porque a definiçao de uma funçao pode receber multiplos parametros, uma chamada 
# de uma funçao pode precisar de multiplos argumentos. Voce pode passar argumentos pras suas 
# funçoes de varias formas. Podemos passar argumentos posicionais, que precisam estar na mesma ordem
# em que os parametros foram escritos. Podemos passar argumentos de palavras reservadas
# onde cada argumento consiste no valor de uma variavel e no seu nome, e podemos passar 
# listas e dicionarios de valores. Vamos explorar cada uma dessas formas: 

# 1) Argumentos posicionais: 

# Quando passamos argumentos pra funçoes, precisamos combinar cada argumento da funçao 
# com um de seus parametros. O jeito mais simples de fazermos isso é usando a ordem que os
# argumentos são passados. Por exemplo: 

def describe_animal(animal_type, animal_name):
    print("I have a " +animal_type)
    print("And its called " +animal_name)

describe_animal('dog', 'harry')

# A definiçao da funçao mostra que precisamos passar o tipo do animal, e o nome do animal, nessa ordem
# Na funçao acima, quando chamamos a funçao, a varivel animal_type vai guardar 'dog' e a variavel
# animal_name vai guardar 'harry'. Se invertessemos a ordem dos parametros, as variaveis iam guardar
# as informaçoes trocadas. 

describe_animal('Tony', 'tiger')

# No exemplo acima vai nos retornar "I have a Tony and its called tiger", porque trocamos a ordem
# dos argumentos. 

# 2) Argumentos chave: 
# Quando passamos argumentos desse jeito, a ordem não vai importar, porque já dissemos qual variavel vai
# receber o que: 

describe_animal(animal_name = "Harry", animal_type="dog")

# Mesmo que invertamos a ordem, Python ja sabe que a variavel animal_name vai receber Harry
# e que a variavel animal_type vai receber dog

# Valores padrao: 
# Os valores padrao sao valores que definimos na definiçao da funçao, e que vao ser usados
# quando nao for passado um parametro para a funçao. Por exemplo, vamos fazer uma funçao 
# e definir um valor padrao 

def greet_friend(friends_name = "Caio"):
    print("Hello " +friends_name)

# Agora, vamos chamar a funçao mas sem dar nenhum argumento

greet_friend()

# Mesmo que nao tenhamos passado nenhum argumento, a função utilizou o valor "Caio"
# que passamos lá em cima. Tem uma coisa sobre usar valores padrao. Vamos fazer isso
# mas com uma função que recebe mais de um argumento 

def cars(car_color, car_type = 'Fiesta'):
    print("I have an " +car_color + " " + car_type)

# Preste atençao que passamos o valor padrao por ultimo. Dessa forma Python pode continuar
# interpretando argumentos posicionais da forma certa 



# Quando passamos MAIS ou MENOS parametros do que a funçao precisa pra fazer o seu trabalho
# Vamos receber um erro. Entao é bom ficar atento aos argumentos que estamos passando pra uma função. 

