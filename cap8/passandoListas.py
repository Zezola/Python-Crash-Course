# Muitas vezes você vai achar útil passar listas pra funções. 
# Quando passamos uma lista pra uma função ela recebe acesso direto aos elementos da lista 

# Digamos que temos uma lista de usuários e queremos imprimir uma saudação pra cada um. 

def greet_all(users):
    for user in users:
        print("Hello " +user)

users = ['Margot', 'Liam', 'Tina']
greet_all(users)

# Podemos também modificar uma lista dentro de uma função. Qualquer modificação que fazemos
# dentro de uma função é permanente, o que nos ajuda muito quando queremos trabalhar com 
# conjuntos grandes de dados. 

# Vamos supor que temos uma lista de livros que queremos comprar. Livros que ja compramos 
# sao separados em uma lista diferente. Podemos organizar o nosso código da seguinte maneira

queroComprar = ["Livro1", "Livro2", "Livro3"]
comprei = []

def compraLivros(nao_comprei, comprei):
    while nao_comprei:
        livro = nao_comprei.pop()
        print("Comprando livro " +livro)
        comprei.append(livro)

def mostraLivros(livros):
    print("\nOs livros seguintes foram comprados: ")
    for livro in livros:
        print(livro)

compraLivros(queroComprar, comprei)
mostraLivros(comprei)

# Nos definimos duas funções. Uma 'compraLivros' que recebe dois argumentos: 
# A lista de livros que queremos comprar, e a lista de livros que já compramos. 
# Ela percorre a lista de livros que queremos comprar, retira os livros, e adiciona
# na lista de livros que já compramos. Ela faz isso até a lista de livros que queremos comprar
# ficar vazia. 
# Ja a segunda funçao é apenas pra imprimirmos os livros que compramos. Ela recebe como argumento
# uma lista de livros, percorre a lista inteira, e imprime cada um dos items dela.
# Nos poderiamos ter feito isso sem usar funções, afinal é um programa pequeno. Mas futuramente
# quando seus programas forem maiores, funções deixam o código bem mais limpo, organizado, e de fácil
# manutenção. 

# Prevenindo que Python modifique uma lista
# As vezes não queremos que uma lista seja modificada ao trabalharmos com ela. 
# Por exemplo ali em cima, se quisessemos guardar a lista de livros que queremos comprar
# como uma referência, não iamos poder, porque esvaziamos ela. Uma das formas que temos
# pra prevenir que isso aconteça é passando uma cópia da lista ao invés da lista original.
# Pra fazermos isso, usamos [:]. Vamos fazer um exemplo parecido com o dos livros 

jogos = ['The Last of Us', 'Doom', 'Guitar Hero']

meus_jogos = []

def compraJogos(jogos, meus_jogos):
    copia = jogos[:]
    while copia:
        jogo = copia.pop()
        print("Comprando: " +jogo)
        meus_jogos.append(jogo)

def mostraJogos(meus_jogos):
    for jogo in meus_jogos:
        print(jogo)

compraJogos(jogos, meus_jogos)
mostraJogos(meus_jogos)

# Mas agora, se formos imprimir a lista original de jogos que ainda não comprei, ela vai 
# permanecer do jeito que estava, porque nós não trabalhamos diretamente com ela, nós
# trabalhamos com uma cópia. 

print(jogos)

# Apesar disso, é uma boa trabalharmos sempre com a lista original, a não ser que tenhamos
# um motivo específico pra trabalharmos com um cópia. 






