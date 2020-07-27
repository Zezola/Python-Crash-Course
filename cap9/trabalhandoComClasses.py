# Na maior parte do tempo vamos estar trabalhando com instancias de alguma classe que criamos
# e um dos trabalhos fundamentais é mudarmos os valores de seus atributos. Podemos mudar eles 
# diretamente, ou podemos escrever um método que muda eles pra gente. 
# Vamos partir pro código e ver isso na prática

class Car():
    ''' Modelo de um carro simples ''' 

    def __init__(self, make, model, year):
        ''' Inicializar os atributos ''' 

        self.make = make
        self.model = model
        self.year = year

    
    def get_long_name(self):
        ''' Retorna uma breve descricao do veiculo '''

        long_name = str(self.year) +" "+ self.model +" "+ self.make
        return long_name.title()
    

meu_carro = Car('audi', 'a4', 2016)
print(meu_carro.get_long_name())

# Aqui, criamos e instanciamos nossa classe Car igual fizemos com a nossa classe Cachorro
# Só que temos uma diferença aqui. Nosso método get_long_name() retorna alguma coisa, já os outros
# não retornavam nada. Toda vez que chamamos um método com retorno, vamos estar acessando a variavel
# ou variaveis que ele retorna. long_name é a variavel que fizemos compondo as informaçoes que temos
# Lembrando que, se estamos trabalhando com coisas que pertencem a classe (make, model, year sao atributos
# que inicializamos no __init__()) temos que colocar self.nome_do_atributo pra acessarmos ele. 

# Definindo valores padrão pra atributos
# Todo atributo em uma classe precisa de um valor inicial, mesmo que esse valor seja 0 ou vazio
# Em alguns casos, faz sentido especificar esse valor no corpo do metodo __init__(). 
# Quando esse atributo vem com um valor de 0 ou vazio, nao precisamos especificar ele nos parametros
# da classe. Vamos modificar um pouco a classe carro e mostrar isso: 

class Car2():
    ''' Modelo de um carro simples ''' 

    def __init__(self, make, model, year):
        ''' Inicializar os atributos ''' 

        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    
    def get_long_name(self):
        ''' Retorna uma breve descricao do veiculo '''

        long_name = str(self.year) +" "+ self.model +" "+ self.make
        return long_name.title()
    
    # Metodo pra modificar o odometro
    def update_odometer(self, miles):
        ''' Modificar o valor do atributo odomer_reading pra um valor que especificamos'''
        self.odometer_reading = miles

    # Metodo que aumenta ou diminui o valor do atributo
    def add_miles(self, miles):
        self.odometer_reading += miles
    
    def read_odometer(self):
        ''' Le o odometro '''
        print("Esse carro ja andou "+str(self.odometer_reading)+ " milhas")

new_car = Car2('Fiat', 'uno', 1998)
print(new_car.get_long_name())
new_car.read_odometer()

# Criamos uma variavel odometer_reading pra dizer quantas milhas o carro andou
# e iniciamos ele com um valor de 0. Repare que nós usamos ele normalmente, mas não
# precisamos indicar ele nos argumentos da classe quando a instanciamos

# Modificando valores de atributos
# Pra modificarmos o valor de um atributo, não podemos acessar ele diretamente e modificar
# Usar um método pra modificar, ou usar um método que faz alguma operacao com o valor do atributo
# Vamos explorar as 3 abordagens

# Modificando diretamente
# Podemos só acessar o valor do atributo e colocarmos o valor que queremos 
new_car.odometer_reading = 20
new_car.odometer_reading = 23

# Usando um método pra modificar
# Dentro da classe mesmo vamos fazer um método pra modificar o atributo que queremos
# Mas ainda sim quando chamamos o método, temos que passar no argumento dele o valor que queremos

new_car.update_odometer(34)
new_car.read_odometer()

# Agora podemos ver que o valor da variavel odometer_reading foi modificado pro valor que
# especificamos no método. 

# Usando um método pra operar o valor
# Podemos ainda ter um método que aumenta ou diminui esse determinado valor mais automaticamente
# Vamos voltar na classe Car2 e criar esse método. 

new_car.add_miles(200)
new_car.read_odometer()

# Agora nosso valor vai ser incrementado em cima do valor que já estava anteriormente. 
# Esses são só alguns de vários jeitos que você pode usar pra modificar os valores dos seus atributos

