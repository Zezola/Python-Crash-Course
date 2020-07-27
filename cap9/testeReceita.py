class Receita():
    def __init__(self, total):
        ''' Init the variables '''
        self.total = total
        self.basico = 0
        self.casa = 0
        self.fun = 0
        self.ed = 0
    

    def get_receita(self):
        ''' Make the finances balance '''
        self.basico = self.total * 0.50
        self.casa = self.total * 0.40
        self.fun = self.total * 0.10
        self.ed = self.total * 0
        receita = {
            "basico": self.basico,
            "casa": self.casa,
            "voce": self.fun,
            "educacao": self.ed
        }

        return receita

    

    def increment_total(self):
        ''' Increment the total by 100 '''
        self.total += 100
    
    def show_receita(self, receita):
        print("Total = " +str(self.total))
        for despesa, quantia in receita.items():
            print(despesa + " = " +str(quantia))


continuar = True

while continuar:
   
    total = int(input("Qual o total que temos na conta: "))
    minha_receita = Receita(total)
    receita = minha_receita.get_receita()
    minha_receita.show_receita(receita)

    pergunta = input("Deseja continuar? (s/n): ")

    if (pergunta.lower() == 's'):
        continuar = True
    elif (pergunta.lower() == 'n'):
        continuar = False
    else:
        print("Resposta invalida. Responda s (sim) ou n (nao)")
        pergunta = input("Deseja continuar? (s/n): ")
    

