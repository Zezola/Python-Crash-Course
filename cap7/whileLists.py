# Ate agora so utilizamos pedaços pequenos de dados
# Mas e se quisessemos mexer com listas e dicionarios??
# Um loop for é efetivo pra percorrer uma lista, mas nao devemos usar ele pra modificar
# uma lista, porque Python vai ter um problema com os valores. Pra modificar uma lista
# a medida que trabalhamos por ela, devemos usar um while 

# Por exemplo, considere uma lista de novos registros em um site que precisam ser verificados
# Depois disso, como podemos separar eles em uma lista dos que nao passaram e dos que passaram?

unconfirmed = ['alice', 'brian', 'ramses']
confirmed = []

while unconfirmed:
    current_user = unconfirmed.pop()

    print("Verifying user "+current_user.title())
    confirmed.append(current_user)

print("The following users have been confirmed:\n")
for confirmed_user in confirmed:
    print("User: "+confirmed_user)

# Removendo instancias especificas de uma lista:
# Podemos usar um while tambem pra remover um valor especifico de uma lista
# Digamos que tenhamos uma lista de cores, onde a cor azul se repete. 
# Queremos tirar o azul da nossa lista de cores. Entao vamos ao codigo: 

cores = ['azul', 'verde', 'roxo', 'vermelho', 'amarelo','azul','cinza']

print(cores)
while 'azul' in cores:
    cores.remove('azul')

print(cores)

# Aqui, apos o primeiro print, ele entrou na condiçao do while (pois ainda tinha um azul na lista)
# E removou o azul encontrado. Ele faz isso novamente até não encontrar mais nenhum

# Montando um dicionario com input do usuario 
# Voce pode pedir o quanto de informaçao pro usuario. Vamos fazer um programa de votacao
# onde pedimos pra cada usuario o seu nome e a sua resposta. 

respostas = {}

# Vamos setar uma flag pro nosso codigo parar 
active = True

while active:
    name = input("Qual seu nome ")
    resposta = input("Qual sua linguagem de programacao preferida: ")

    #Guardar as respostas no dicionario 
    respostas[name] = resposta

    #Verifica se vamos continuar no loop
    repeat = input("Mais alguem quer responder? (yes or no)")
    if repeat == 'no':
        active = False
    
# Mostrar os resultados 

for nome, resposta in respostas.items():
    print("Seu nome e " +nome+ " e sua linguagem preferida e "+resposta)