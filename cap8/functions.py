# Nesse capitulo vamos aprender sofre funçoes. Funçoes sao blocos de codigos especificos 
# pra fazer uma ação específica. Dessa forma, se tiver alguma coisa que você precisa repetir
# no código, você pode só chamar a função e Python vai rodar o código que está dentro dela
# Vamos aprender também a guardar funções em arquivos separados chamados módulos, pra organizar
# melhor as nossas aplicações. 

# Definindo uma função: 

# Funções começam com a palavra reservada def, e depois do nome que vamos dar pra elas.
# é uma boa pratica dar nomes bem auto explicativos pras nossas funções. Por exemplo, vamos
# fazer uma função que recebe dois parametros e devolve a soma entre esses dois parâmetros. 

def soma(a,b):
    return a + b

print(soma(2,3))

# Os valores dentro dos parenteses sao chamados de parametros da funçao. Parametros da funçao
# sao os valores que ela precisa pra trabalhar. Podemos ter funções sem parametro, mas os parenteses
# ainda sao necessarios. 

def saudacao():
    print("Ola")

saudacao()