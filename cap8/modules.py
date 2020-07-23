# Uma das vantagens de usar funções é como elas separam nosso código em blocos
# específicos. Nós ainda podemos ir um pouco além, e guardar nossas funções em um arquivo separado
# e importar ela pro nosso programa. Dessa forma escondemos os detalhes de implementação
# Esse arquivo separado vai ser chamado de modulo, e importar ele pro nosso programa 
# quer dizer que estamos "liberando" o acesso a esse modulo. Isso nos permite também usar
# uma mesma função em vários programas diferentes sem ter de reescrever ela toda vez que 
# estamos usando. Importar modulos pro nosso programa também nos permite usar código escrito
# por terceiros em nossos programas. 

# Podemos importar um modulo inteiro: 
# Pra criar um modulo, precisamos de um arquivo com a extensao .py no final dele.
# Vamos criar um modulo com a funçao make_pizzas() que usamos anteriormente. 
# Ok, agora vamos importar esse modulo pra cá. 

import pizza

# E agora vamos usar a funçao make_pizza()

pizza.make_pizza('peperonni')
pizza.make_pizza('cheese', 'bacon')

# Quando esse arquivo é interpretado, Python procura o arquivo pizza.py, e importa suas funçoes
# pra esse arquivo. Só que não podemos só sair usando. Temos que dizer de onde essa função está vindo.
# por isso que antes de chamarmos a função, colocamos o nome do modulo. A notação ponto (o '.' antes do nome da funçao)
# Está basicamente falando "Puxe do modulo pizza a funçao make_pizza()"

# Importando funções específicas: 

# Podemos também importar uma função específica de um determinado modulo. Vamos fazer outro modulo
# e importar uma funçao especifica dele. 
# Criamos o modulo car.py. Vamos importar a funçao make_car() dele. 

from car import make_car 

# Essa linha de codigo a cima basicamente diz "Do modulo X importe as funçoes Y"
# podemos importar quantas funçoes quisermos de um determinado modulo. 
# Agora podemos usar a funçao make_car() 

make_car("Honda", "Civic", "black")

# Quando importamos uma funçao espefica, não precisamos usar a notação ponto, 
# pois o interpretador já sabe de onde essa função veio. 

# Dando um apelido aos nossos imports 

# Poderiamos dar um apelido as coisas que importamos, por questões de comodidade
# e legibilidade do nosso codigo. Vamos fazer outro modulo e importar, mas dessa vez com um
# apelido. Criamos o modulo profile.py. Agora vamos importar pra cá a funçao make_profile()
# mas com o apelido de mp. 

from profile import make_profile as mp

# Python é bem intuitivo, lendo a linha acima ja temos uma ideia do que estamos fazendo.
# Estamos dizendo "de profile importe make_profile como mp"
# Agora podemos usar a funçao make_profile, mas como mp. 

mp("Jose", "Ulisses", 24)

# Da mesma forma que podemos usar 'as' pra dar um nome a uma funçao, podemos fazer isso
# pra dar um nome a um modulo todo. 

# Importando todas funções em um modulo: 

# Podemos importar TODAS funções em um modulo simplesmente usando "*"
# A sintase pra isso é "from module_name import *"
# É uma boa ideia não usarmos isso pra modulos muito grandes que vieram de terceiros, 
# Pois se o nome de uma função do modulo bater com o nome de uma funçao que já existe
# no nosso codigo, podemos ter alguns resultados indesejaveis. 

# OBS: Temos algumas boas praticas pra funçoes e imports. 
# 1) Nomes de funçoes devem ser em letra minuscula e separados por underscore
# 2) Toda funçao deve ter um comentario logo no inicio no formato docstring (''' coment ''')
# 3) Funçoes devem ter nomes descritivos e seus comentarios devem ser bem explicitos sobre o que ela faz
# 4) Se voce especificar um valor padrao pra um argumento, nenhum espaço deve ser usado em nenhum dos lados do sinal de igual 
# 5) imports devem vir no começo do codigo
# 6) Se os parametros de uma funçao deixarem a definiçao maior que 79 caracteres, devemos pular uma linha
# e dar dois tabs de espaço. 
# 7) Se seu programa ou modulo tem mais de uma funçao, podemos separar cada uma por 2 linhas