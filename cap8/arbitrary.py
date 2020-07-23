# As vezes não vamos ter como saber direito quantos argumentos vamos ter que passar
# pras nossas funções. Felizmente em Python nós temos um jeito simples de lidar com esse
# tipo de situação. Adicionamos * antes do parametro. Dessa forma, Python faz uma tupla vazia
# com o nome que dermos ao parametro, e vai adicionando os valores que receber dentro dessa tupla
# Vamos fazer o exemplo das pizzas: 

def make_pizza(*toppings):
    print(toppings)

make_pizza('peperonni')
make_pizza('olives', 'mushrooms', 'cheese')

# Ok agora vamos dar uma mexida na função pra ela imprimir o topping que estamos colocando
# na pizza, como fizemos nas anteriores

def make_pizza2(*toppings):
    for topping in toppings:
        print("Adding " +topping)
    print("Your pizza is ready")

make_pizza2('mushrooms', 'peperonni', 'shrimp')
make_pizza2('cheese')

# Misturando argumentos posicionais e arbitrários

# Nós podemos usar tanto argumentos posicionais como argumentos arbitrários nos nossos programas
# Vamos fazer uma outra função de fazer pizzas, só que dessa vez vamos passar também o tamanho da pizza

def make_pizza3(size, *toppings):
    print("Making a " +str(size) + "cm pizza with the toppings:")
    for topping in toppings:
        print("-"+topping)
    print("Your pizza is ready")

make_pizza3(30, 'cheese', 'mushrooms')

# Só temos que colocar o argumento arbitrário no final, porque primeiro python verifica 
# os argumentos posicionais, os palavras-chave, e depois ele verifica os outros tipos de argumento

# Usando argumentos palavra-chave arbitrários

# As vezes você quer aceitar argumentos arbitrários pra uma função, mas não temos certeza
# de que tipo de informação vamos receber. Nesses casos, podemos escrever funções que aceitam
# quantos pares chave-valor passarmos pra ela. Um exemplo é construir perfis de usuários. 
# Nós sabemos que vamos receber informação do usuario, mas não temos certeza de que tipo de
# informações vamos receber. A função a seguir mostra um exemplo desse tipo de situação

def construir_perfil(primeiro, ultimo, **info):
    perfil = {}
    perfil['nome'] = primeiro
    perfil['sobrenome'] = ultimo
    for chave, valor in info.items():
        perfil[chave] = valor
    return perfil

perfil = construir_perfil('Carlos', 'Alberto', local = 'maria paula', campo = 'data science')

print(perfil)

# A definiçao da nossa funçao de construir usuarios espera um primeiro e ultimo nome, e depois
# permite que coloquemos o quanto de pares chave-valor precisarmos colocar. Os dois asteristicos
# antes do nome do parametro informam ao python que ele precisa criar um dicionario vazio chamado info
# e colocar qualquer par chave-valor que passarmos dentro desse dicionario. Dentro da funçao
# podemos acessar os valores desse dicionario. 
# No corpo da funçao, criamos um dicionario vazio chamado perfil pra guardar as informações 
# do usuário. Depois colocamos o primeiro e o ultimo nome, que são parametros que sempre vamos
# passar, dentro do dicionário. Após isso nós fazemos um loop que percorre o restante dos pares
# chave-valor que colocamos e vamos os passando pra dentro do dicionario. 
# Apos isso, retornamos o dicionario já pronto. 


