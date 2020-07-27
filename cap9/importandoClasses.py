# A medida que vamos adicionando mais funcionalidades as nossas classes, nossos arquivos
# começam a se tornar grandes, mesmo que usemos herança direito. 
# Seguindo a filosofia do Python, queremos manter nossos arquivos os mais sucintos possiveis
# Pra isso temos a possibilidade de guardar classes em módulos e importa-las quando precisarmos

# Importando uma classe só 
# Vamos criar um módulo que só contem a classe Carro
# Chamamos esse módulo de car.py
# Agora vamos criar um arquivo para importarmos esse módulo. Vamos chamar de my_car.py
# Importar classes é um jeito eficiente de programar, porque deixa nosso arquivo principal
# o mais limpo e curto possível. Você também guarda a lógica do seu programa em arquivos
# separados, então quando todas as classes funcionarem do jeito que queremos podemos 
# nos preocupar com os detalhes de implementação no arquivo principal.


# Guardando multiplas classes em um modulo
# Voce pode guardar quantas classes quiser em um módulo. 
# Por exemplo, podemos criar uma classe Bateria e a classe CarroEletrico no nosso arquivo
# car.py 
# Fazemos um novo arquivo chamado my_eletric_car.py, e nele importamos somente a classe
# CarroEletrico do arquivo car.py. O comportamento vai ser o mesmo que se tivessemos escrito
# a classe normalmente dentro do arquivo. 

# Importando varias classes de um modulo
# Voce pode importar quantas classes precisar em um arquivo. Se nós quisessemos fazer um carro
# normal e um carro eletrico no mesmo programa, podiamos simplesmente importar as duas classes
# nesse mesmo arquivo. Vamos criar um arquivo chamado my_cars.py e fazer isso nele. 


# Importando o módulo todo
# Você pode também importar o modulo inteiro pra dentro do arquivo e usar as classes que estão nele.
# É uma abordagem simples e resulta em código que é limpo e fácil de ler. Cada vez que instanciamos
# uma classe dessa forma, temos que colocar o nome do modulo e a notaçao ponto. Dessa forma você
# não vai ter problemas com nomes dando conflito. Vamos fazer isso no arquivo my_cars.py

# Importando um módulo dentro de um módulo
# As vezes vamos querer espalhar nossas classes em varios arquivos pra impedir que um arquivo
# fique grande demais. Quando fazemos isso, as vezes vamos ver que uma classe depende de outra classe
# que está em outro módulo. Quando isso acontece, você pode importar 
# Por exemplo, vamos guardar a classe Car em um modulo, e as classes CarroEletrico e Bateria em outro
# Só que a classe CarroEletrico precisa ter acesso a classe Pai, que é a classe Car. 
# Entao importamos ela no modulo
# Agora podemos criar os modulos separadamente e criar o carro que precisamos
# Vamos mudar isso no arquivo my_cars.py

