# Programação Orientada a Objetos é uma das formas mais eficientes de escrevermos software. 
# Na programação orientada a objetos, escrevemos classes que representam coisas do mundo real. 
# Quando você escreve uma classe, você define o comportamento de todo um conjunto de objetos.
# E quando criamos um objeto a partir de uma classe, todos objetos que criarmos a partir dessa classe
# vão ter uma série de comportamentos e caracteristicas gerais que definimos na classe. 
# A partir daí você pode adicionar traços unicos em cada um se desejado com só algumas linhas de código.
# Fazer um objeto a partir de uma classe se chama instanciar a classe, e você trabalha com instancias de uma classe.
# Vamos escrever classes e instancia-las. Vamos específicar que tipo de informação vai ficar guardada nessas instancias
# e especificar comportamentos pra trabalhar com essas informações. 
# Quando você programa orientado a objetos, você entende melhor o seu código, não só o que acontece
# linha por linha, mas os conceitos gerais. Além disso as classes podem ser compartilhadas com outros 
# programas, fazendo a vida mais fácil pra você e outros programadores que forem trabalhar com você. 

# Criando e usando uma classe 
# Podemos modelar quase qualquer coisa utilizando classes. Por exemplo, vamos fazer uma classe
# que modela um cachorro. Mas a classe é apenas um modelo. Você não está modelando um cachorro em especifico
# você está modelando um cachorro no geral. A partir desse modelo, você pode criar vários objetos do tipo
# cachorro. 

class Cachorro():
    ''' Uma tentativa de modelar um cachorro ''' 

    def __init__(self, name, age):
        ''' Inicializando o nome e a idade '''
        self.name = name
        self.age = age
    

    def sit(self):
        ''' Simular o comando de sentar ''' 
        print(self.name.title() + " is now sitting")
    

    def roll(self):
        ''' Simular o cachorro rolando ''' 
        print(self.name.title() + " rolled over")


# No começo do codigo acima, definimos uma classe chamada Cachorro. Por convenção, nomes de 
# variáveis começam com letra maiuscula. 
# Uma coisa esquisita logo no começo da clase é esse metodo __init__()
# metodos são funções que estão dentro de uma classe. 
# O método __init__() ( Dois underlines no começo e dois no final) é um método especial 
# que Python trás pra nós. Ele vai ser chamado automaticamente toda vez que criamos um objeto
# a partir dessa classe. Os underlines são pra garantir que o nome desse método não vai 
# bater com o nome de nenhum método criado por você. 
# Nós definimos ele com 3 parametros. self, name, e age. O parametro self é mandatório 
# do próprio método e precisa vir antes dos outros. Os outros dois, age e name, são parametros
# normais que criamos. Quando chamamos o self, isso dá ao objeto acesso aos atributos e métodos
# dentro da própria classe. 
# As duas variáveis que definimos dentro do __init__() vem na forma self.variavel. 
# Toda variável que vem com o prefixo self estão disponiveis pra todos os métodos da classe.
# self.name = name pega o valor que esta no parametro name e liga ela a variavel name,
# que depois é ligada a instancia da classe que foi criada. 
# Depois, temos dois metodos. sit e roll. Eles não precisam de informaçao extra, então só passamos
# a variavel self, que vai permitir que as instancias que criamos depois tenham acesso a esses métodos. 
# Agora vamos instanciar a classe Cachorro. 

meu_cachorro = Cachorro('Lua', 12)

print("Nome do cachorro = " +meu_cachorro.name.title())
print("Idade = "+str(meu_cachorro.age))

# a classe Cachorro que estamos usando aqui é a que escrevemos ali em cima. 
# Quando declaramos a variavel meu_cachorro e chamamos a classe Cachorro passando os atributos
# nome e idade, Python automaticamente chama o metodo __init__() dentro dessa classe, e associa 
# os valores que passamos as variaveis name e age que estão dentro da classe. A convenção pra escrever
# nomes de classes ajuda aqui, porque quando vemos uma variavel começando com letra maiuscula, sabemos
# que ela é uma classe que está sendo instanciada. 


# Acessando atributos
# Pra acessar atributos de uma instancia, usamos a notação ponto da seguinte forma:
# nome_do_objeto.atributo 
# o mesmo vale pra métodos. 

print(meu_cachorro.age)
print(meu_cachorro.name)
meu_cachorro.roll()
meu_cachorro.sit()


# Criando multiplas instancias de uma classe 
# Uma das grandes vantagens de usarmos classes é que podemos criar várias instancias
# de uma mesma classe de forma rápida e eficiente. 

cachorro1 = Cachorro('Lucy', 2)
cachorro2 = Cachorro('Mabel', 8)

# Podiamos continuar criando quantos cachorros quisessemos e acessar todos seus metodos
# e atributos normalmente. 

print("O nome desse cachorro é " +cachorro1.name.title())
print("E ele tem " +str(cachorro1.age)+" anos")
cachorro1.sit()

print("O nome daquele cachorro é " +cachorro2.name.title() )
print("E ele tem " +str(cachorro2.age)+" anos")
cachorro2.sit()

# Mesmo que criemos varios cachorros com os mesmos nomes e idades, ainda sim Python 
# vai dar uma instancia separada pra cada um, desde que o nome do objeto seja diferente. 