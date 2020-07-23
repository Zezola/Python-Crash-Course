# Uma funçao nem sempre tem que retornar uma mensagem diretamente. Ela pode trabalhar com algum dado
# e depois retornar um ou mais valores. O valor que a função retorna é chamado de valor de retorno
# O comando return pega um valor de dentro da função e envia ele de volta pra linha que chamou a função
# Valores de retorno permitem que muito do trabalho do nosso codigo seja feito dentro das funções
# deixando o corpo do codigo mais limpo e mais facil de dar manutenção. 

# Retornando um valor simples 
# Vamos usar uma funçao pra formatar um nome e retornar o valor formatado. 

def get_formated_name(first_name, last_name):
    """ Retorna o nome completo de uma pessoa """ 
    full_name = first_name + " " +last_name
    return full_name

musician = get_formated_name('jimi', 'hendrix')
print(musician)

# Aqui usamos uma funçao pra formatar um nome, depos retornamos o nome já formatado 
# que foi guardado dentro da variavel full_name. Quando você chama uma função que retorna 
# um valor, você precisa de uma variável onde esse valor de retorno vai ser guardado. 

# Tornando um argumento opcional
# As vezes faz sentido tornarmos um argumento opcional e só usarmos se o usuário passar. 
# Se pegarmos a função que temos ali em cima, e dermos a ela um argumento extra, por exemplo
# ela ficaria assim: 

def get_formated_name2(first_name, middle_name, last_name):
    full_name = first_name + " " + middle_name + " " + last_name
    return full_name.title()

nat = get_formated_name2("Natthaya", "julia", "lindstrom")
print(nat)

# Ela ia funcionar se quisessemos passar o nome do meio de alguem. Mas e se a pessoa não tiver
# ou nao quiser passar? Nosso programa não ia funcionar, mesmo que a função esteja escrita corretamente. 
# Pra resolver isso, podemos dar ao parametro que queremos que seja opcional um valor padrão vazio 
# e coloca-lo depois dos outros parametros

def get_formated_name3(first_name, last_name, middle_name=""):
    full_name = first_name + "" + middle_name + " " + last_name
    return full_name.title() 

pessoa = get_formated_name3("Marcos", "Ribeiro")
print(pessoa) 

# Nesse exemplo a nossa função vai sempre receber um ultimo e primeiro nome, já o nome do meio
# é opcional, então declaramos ele por ultimo, e passamos um valor padrão vazio pra ele

# Retornando um Dicionario
# Funçoes podem retornar qualquer valor que você precisar, inclusive estruturas de dados mais
# complicadas, como listas e dicionários. Vamos fazer uma função pra "construir" uma pessoa 
# e retornar um dicionario 

def build_person(first_name, last_name):
    person = { 'first': first_name, 'last': last_name}
    return person

pessoa1 = build_person('Cezar', 'Coelho')
print(pessoa1)

# A funçao acima recebe um primeiro nome e um ultimo nome e guarda eles em um dicionario
# a chave 'first' recebe o primeiro nome, e a chave 'last' recebe o ultimo nome, depois 
# retornamos o dicionario ja pronto 
# Podemos modificar essa funçao pra receber um parametro opcional da mesma forma que fizemos
# com as outras 

def build_person2(first_name, last_name, age = ''):
    # Se age for passado, vamos adiciona-la ao dicionario
    person = { 'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person 

pessoa2 = build_person2('Ana', 'Lucia', 25)
print(pessoa2)

# Podemos usar funções combinadas com qualquer coisa
# Por exemplo, vamos usar um loop while pra receber informações sobre um usuario 
# e mostrar uma mensagem personalizada pra ele. 

def full_name(first_name, last_name):
    full_name = first_name + " " +last_name
    return full_name.title()

while True:
    print("\nPlease tell us your name: ")
    print("(enter 'q' anytime to quit ")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    name = full_name(f_name, l_name)
    print("Hello, " +name)