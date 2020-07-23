# Programa que faz uma votaçao entre 3 linguagens, e no final mostra o numero de votos de cada uma

pessoas = []

linguagens = {
    "Python": 0,
    "C": 0,
    "Java": 0
}



flag = True 

while flag:
    nome = input("Qual o seu nome: ")
    pessoas.append(nome)
    lang = input("Escolha entre python, C, ou java: ")
    if (lang.lower() == 'python'):
        linguagens["Python"] += 1
    elif (lang.lower() == 'c'):
        linguagens["C"] += 1
    elif (lang.lower() == 'java'):
        linguagens["Java"] += 1
    else:
        print("Resposta invalida, por favor, digite uma resposta valida.\n")
        lang = input("Escolha entre python, c ou java\n")
    continuar = input("Mais alguem vai responder? [Y/N]")
    if (continuar.upper() == 'N'):
        flag = False
    elif(continuar.upper() == "Y"):
        flag = True
    else:
        print("Resposta invalida. Responda com Y ou N")
        continuar = input("Mais alguem vai responder? [Y/N]")

print("--- Resultados ----\n")

for lang, votos in linguagens.items():
    if (votos == 0):
        print(lang + ": Nenhum voto")
    if (votos == 1):
        print(lang + ":" +str(votos)+" voto")
    else:
        print(lang + ":" +str(votos)+ " votos")




    