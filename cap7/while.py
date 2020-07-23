# Vamos aprender sobre o laço while agora. 
# While significa enquanto. 
# Ele vai rodar um trecho de codigo ENQUANTO dada condicao for verdadeira. 
# Por exemplo, queremos rodar um trecho que imprime um numero ENQUANTO esse numero
# for MENOR que 10. 

num = 1
while (num < 10):
    print(num)
    num += 1 
print("Saindo do loop")

# O while verifica se a condiçao é verdadeira toda vez antes de ir pro loop. 
# Entao no programa acima ele vai verificar se o valor de num é MENOR que 10.
# se for, ele roda o trecho de codigo. Aumentamos o valor da variavel num ali em baixo
# porque se nao, num ia ser menor que 10 pra sempre. E nosso loop ia continuar pra sempre
# o que não é o comportamento desejado dos nossos programas. 
# ele vai verificar toda vez a condiçao antes de entrar no loop. Se uma hora a condiçao for falsa
# ele vai sair do loop e continuar executando o codigo normalmente

# Deixando o usuario escolher quando sair do programa

# Ate agora, nossos programas acabavam assim que determinada açao acontecia.
# mas e se temos um programa que continua rodando e o usuario escolhe quando quer sair?
# um jogo, por exemplo. Podemos usar o valor de algum input do usuario como o nosso 'sinal'
# para encerrar o programa. 

msg = "Digite uma msg e eu vou repetir\n"
msg += "Digite sair pra sair do programa\n"

num = input(msg)

while (str(num) != 'sair'):
    print(num)
    num = input(msg)

# Usando uma Flag 

# Nos programas passados, nossas condiçoes eram bem simples. 
# Mas e quando estamos trabalhando com um conjunto maior de possibilidades que 
# fariam o programa parar de rodar. Em um jogo por exemplo, pode ser quando 
# todas as vidas do jogador acabarem, ou enquanto o jogador nao digitar quit, ou 
# caso o objetivo que ele deveria proteger foi destruido, etc...
# Para isso, podemos usar uma flag para sinalizar pro nosso programa se ele deve ou nao
# continuar rodando. Uma flag é geralmente uma variável que recebe True ou False. 
# E quando alguma das condiçoes pro programa rodar não é satisfeita, o valor da nossa Flag mudaria
# dessa forma a unica comparacao que fariamos dentro do nosso while é se a flag é verdadeira ou nao. 

prompt = "\nTell me something and i'll repeat"
prompt += "\nEnter quit to quit the program\n"

active = True 
while active:
    repeat = input(prompt)
    if (repeat == 'quit'):
        active = False
    else:
        print(repeat)

# Nos usamos a flag active, e começamos ela com o valor inicial de True
# assim nosso programa vai rodar pelo menos uma vez. Enquanto essa variavel continuar dando
# True, nosso programa vai continuar rodando. Dentro do while, nos checamos para a condiçao
# que causaria a mudança no valor da nossa flag. Caso ele aconteça, nossa flag muda pra false
# e nosso programa para. Caso nao, ele vai continuar seguindo a rotina do programa

# Saindo de um while com um break 
# Podemos sair de um laço while imediatamente sem correr nem outro codigo 
# no loop usando a palavra reservada break. break controla o fluxo do seu codigo,
# e sai de qualquer loop assim que o programa chega nele. Vamos usar agora

num = int(input("Digite um numero e diremos se e par ou impar. \n Digite -1 pra sair"))

while True:
    if (num == -1):
        break
    elif (num % 2 == 0):
        print("Par")
        num = int(input("Digite um numero e diremos se e par ou impar. \n Digite -1 pra sair\n"))
    else:
        print("Impar")
        num = int(input("Digite um numero e diremos se e par ou impar. \n Digite -1 pra sair"))

# Um loop que comece com True (while True) vai rodar infinitamente a nao ser que ele encontre
# um break em algum lugar dentro dele. 

# Usando continue dentro de um loop 
# Ao invez de sair de um loop sem executar o resto do seu codigo, podemos usar a palavra reservada
# continue pra retornar pro inicio do loop baseado no resultado de um teste condicional.
# Por exemplo, e se quisermos imprimir os numeros de 1 a 10, mas so os pares

current_number = 0 
while current_number < 10:
    current_number += 1
    if current_number % 2 != 0:
        continue 
    print(current_number)

# Quando ele encontra algum numero impar, ele bate no continue e volta pro começo do loop. 
