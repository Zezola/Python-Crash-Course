# Nem sempre precisamos começar do 0 ao escrever uma classe. Se a classe que vamos escrever
# é uma versão mais especializada de uma classe que já existe, podemos usar heranca.
# Quando uma classe herda de outra classe, dizermos que a classe que está herdando é a classe
# filho, e a classe original é a classe pai. A classe filho vai herdar todos os métodos e
# atributos da classe pai. Mas também é livre pra ter seus próprio atributos e métodos. 

# Quando usamos herança, a primeira missão do interpretador do Python é passar os atributos
# e métodos da classe pai pra classe filho. Pra isso, o método __init__() da nossa classe filho
# vai precisar de uma ajuda da classe pai. Vamos voltar ao nosso exemplo do carro. Só que agora
# vamos fazer uma classe Carro normal, e uma classe CarroEletrico. A classe CarroEletrico()
# é só um carro de um tipo específico. Então, podemos criar essa classe baseada na nossa clarro Carro()


class Carro():
    def __init__(self, make, model, year):
        ''' Initialize the attributes '''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 
    

    def read_odometer(self):
        ''' Print the odometer reading '''
        print("This car have " +self.odometer_reading+ " on it")
    
    def set_odometer_reading(self, miles):
        ''' Set the odometer_reading to an specific value '''
        self.odometer_reading = miles

    def increment_odometer_reading(self, miles):
        ''' Increment the odometer_reading by an specific value '''
        self.odometer_reading += miles
    
    def get_full_name(self):
        full_name = self.make + " " + self.model + " " +str(self.year)
        return full_name

class Bateria():
    ''' Uma bateria simples '''

    def __init__(self, tamanho_bateria = 70):
        ''' Inicializar os atributos '''
        self.tamanho_bateria = tamanho_bateria
    
    def descreve_bateria(self):
        ''' Imprime informaçoes sobre a bateria '''
        print("A bateria desse carro tem " +str(self.tamanho_bateria)+ "-kWh") 
    
    def get_max(self):
        if (self.tamanho_bateria == 70):
            maximo = 120
        elif (self.tamanho_bateria == 80):
            maximo = 130
        
        msg = "O carro pode ir a " +str(maximo)+ " com a bateria cheia"
        print(msg)

class CarroEletrico(Carro):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.bateria = Bateria()

my_tesla = CarroEletrico('tesla', 'model s', 2016)
print(my_tesla.get_full_name())




# Quando você cria uma classe filha, a classe pai deve estar presente no arquivo e vir 
# antes da classe filha. Nós definimos a subclasse CarroEletrico, e passamos entre os parenteses
# a classe Carro. E o método __init__() pega a informação necessária pra fazermos uma instancia
# da classe Carro. A funçao super() no começo do método __init__() faz a ligação entre a classe filha
# e a classe pai. O nome super vem de uma convenção de chamar a classe original de superclasse
# e a classe filha de subclasse. Nós testamos pra ver se a herança está funcionando direito
# criando uma instancia da classe CarroEletrico, e passamos todos atributos que uma classe Carro
# ia ter. No momento, a classe CarroEletrico ainda não tem métodos ou atributos que são particulares
# a ele. 

# Definindo atributos e métodos pra classe filha. 
# Uma vez criada a nossa classe filha, nós podemos ter métodos e atributos que são particulares
# a ela. 

class Pai():
    def __init__(self, cabelo, olhos):
        self.cabelo = cabelo
        self.olhos = olhos
    
    def show_attributes(self):
        print("O pai tem olhos " +self.olhos)
        print("O pai tem cabelo " +self.cabelo)
        print("Nao tem tatuagem")
    
    def assistir_futebol(self):
        print("Cervejinha e gol do gabigol")
    

class Filho(Pai):
    def __init__(self, cabelo, olhos):
        super().__init__(cabelo, olhos)

        ''' Definindo atributos que só o filho tem '''
        self.tatuagem = True
    
    def show_attributes(self):
        print("O filho tem olhos " +self.olhos)
        print("O filho tem cabelos " +self.cabelo)
        if self.tatuagem:
            print("Tem tatuagem")
    
    def assistir_futebol(self):
        print("Na verdade não gosto de futebol")

# No código acima, escrevemos duas classes. Uma classe chamada Pai e uma classe chamada Filho.
# Quando fazemos a heranca, a classe Filho vai ter tudo que a classe Pai tem. Só que criamos
# um atributo a mais na classe Filho, a tatuagem. Ele vai estar presente só na classe filho
# Vamos instanciar e ver como funciona 

pai = Pai('castanho', 'castanhos')
filho = Filho('castanho', 'azuis')

pai.show_attributes()
filho.show_attributes()

# Na classe filho, quando vamos definir um atributo que só ela tem, nós adicionamos
# no método __init__() um novo atributo com um valor inicial definido. Não tem um limite
# do quanto podemos criar na classe filho, podendo deixar ela muito mais específica do que
# a sua classe pai. 

# Sobreescrevendo metodos da classe pai
# Você pode sobreescrever um método da classe pai que não faça sentido no que queremos
# modelar na classe filha. Pra fazer isso, nós criamos um método na classe filha que tenha
# o mesmo nome do método que existe na classe pai. Python vai ignorar o método da classe pai
# e considerar só o método da classe filha. Voltando no exemplo que criamos ali em cima, 
# vamos adicionar um metodo assistir_futebol() na classe Pai. Já o Filho não curte futebol
# então podemos mudar esse método dentro da classe filho. Agora se alguém tentar chamar o
# método assistir_futebol() da classe filho, Python vai ignorar o método da classe Pai
# e vai olhar só pro método da classe filho. 

# Instancias como atributos 
# Quando estamos modelando algo do mundo real em uma classe, as vezes nos vemos
# adicionando cada vez mais e mais atributos, nosso arquivo ficando maior e maior.
# Nesse tipo de situação, você pode reconhecer que alguns desses atributos podem ser
# quebrados em classes separadas. 
# Por exemplo, na classe CarroEletrico() nós podemos acabar percebendo que estamos
# adicionando vários métodos e atributos que tem a ver com a bateria do carro. 
# Poderiamos criar uma classe separada pra bateria, e adicionar esses métodos e atributos
# dentro dessa classe
# A classe que vamos usar como atributo deve vir ANTES da classe que vai receber esse
# atributo. Agora podemos chamar o atributo bateria dentro da classe CarroEletrico, e 
# acessar seus metodos e atributos a partir dessa classe. 
# Pode parecer que é muito trabalho a mais, só que agora podemos trabalhar com os
# atributos e métodos relacionados a bateria do carro sem poluir a nossa classe CarroEletrico

meu_carro_eletrico = CarroEletrico('tesla', 'model s', 2019)

print(meu_carro_eletrico.get_full_name())
meu_carro_eletrico.bateria.descreve_bateria()

# Vamos voltar em Bateria() e adicionar um outro método pra dizer o quanto o carro consegue
# atingir em km/h baseado no tamanho da sua bateria

meu_carro_eletrico.bateria.get_max()

# Lembrando que, toda vez que queremos chamar algum atributo ou método que criamos
# na classe Bateria(), nós temos que fazer isso pelo atributo bateria que criamos
# na nossa instancia meu_carro_eletrico. 


# Modelando Objetos Reais
# A medida que vamos tentando modelar coisas mais complexas, esbarramos com algumas questoes
# interessantes. No CarroEletrico, por exemplo, a velocidade maxima é um atributo da bateria
# ou do carro? 
# Quando tentamos modelar um objeto real, não estamos pensando tanto em Python, mas sim em 
# como esse objeto funciona. Muitas vezes vamos escrever e reescrever uma classe inteira
# pra lidar com as questões que vão surgindo a medida que escrevemos a nossa classe. 

