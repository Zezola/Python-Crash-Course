# Python ja vem com um conjunto de modulos incluidos. Agora que temos um entendimento
# basico de classes e modulos, vamos dar uma olhada em alguns

# Vamos começar com o OrderedDict 
# Dicionarios permitem que guardemos pedaços de informaçao mas não mantem uma ordem entre eles
# Se voce criou um dicionario e quer manter a ordem em que os valores são adicionados, podemos
# usar a biblioteca collections e puxar o OrderedDict

from collections import OrderedDict

fav_langs = OrderedDict()

fav_langs['peter'] = 'python'
fav_langs['joan'] = 'C'
fav_langs['carlos'] = 'ruby'

for name, lang in fav_langs.items():
    print(name.title() + "'s favourit language is " +lang)

# Começamos importando a classe OrderedDict do modulo collections
# Depois criamos uma instancia da classe, e guardamos ela com o nome de
# fav_langs. Quando instanciamos OrderedDict ele já cria pra nós um dicionario
# ordenado. Depois adicionamos pares chave-valor ao nosso dicionario,
# e agora quando formos imprimir, vamos ter sempre os valores na ordem em que foram
# adicionados ao dicionario
# Isso é só um dos exemplos do que a biblioteca normal do Python nos dá. A medida que formos
# criando nossas aplicações vamos ver a necessidade de encontrar e usar novas bibliotecas.
