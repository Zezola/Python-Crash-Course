# A maioria dos programas que criamos sao feitos pra resolver um problema do usuario
# E pra isso vamos precisar que o usuario nos de alguma informacao. 
# Pra isso vamos aprender a usar a funçao input() do python. 
# E vamos aprender tambem a usar um loop while pra um trecho de codigo continuar
# rodando enquanto uma certa condiçao for verdadeira, dessa forma permitindo que o 
# usuario coloque o quanto de informação for necessário pro programa. 

# Como o metodo input() funciona?
# Ele pausa o programa e espera o usuario digitar alguma coisa, depois salva em uma variavel
# pra ficar mais facil de trabalharmos com essa informação. 

message = input("Digite alguma coisa e eu vou repetir pra voce: ")
print(message)

# input() recebe um parametro: As intruções que estamos dando pro usuario sobre o que ele 
# deve digitar. No exemplo acima, as instruçoes sao pro usuario digitar algo. O programa 
# guarda essa informação dada pelo usuario numa variavel chamada message. 
# Toda vez que pedimos informaçao pra um usuario, devemos dar a ele instruçoes claras 
# e precisas do que ele deve digitar

nome = input("Digite o seu nome: ")
print("Ola "+nome)

# As vezes queremos dar mensagens maiores e mais explicativas pro usuario. Podemos 
# guardar essa mensagem em uma variavel e passar ela como parametro pra funçao input() 

prompt = "Digite o seu nome e vamos dize-lo de volta pra voce."
prompt += "\n Entao, qual o seu nome?\n"

name = input(prompt)
print("Bom dia, " +name+ " !")

# Aceitando numeros

# As vezes queremos pedir um dado numerico pro usuario, como sua idade por exemplo. 
# Só que a funçao input() interpreta tudo que o usuario entrar como string. Entao 
# se fossemos tentar trabalhar com a idade, que é um numero, iamos encontrar algum erro
# no nosso programa. Pra isso precisamos transformar a entrada do usuario no tipo de dados
# que queremos. Por exemplo, se queremos um inteiro, usamos a funcao int() e colocamos a 
# funçao input() dentro dela. 
# int(input(blabla))

msg = "Para entrar nesse site precisa ser maior de 18 anos.\nPrecisamos saber sua idade"
msg += "\nQual a sua idade:\n"

idade = int(input(msg))

if (idade >= 18):
    print("Pode entrar")
else:
    print("Nao pode entrar")

