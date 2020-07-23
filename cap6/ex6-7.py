pessoa1 = {
    "nome": "Jaime",
    "idade": "320"
}

pessoa2 = {
    "nome": "Lucas",
    "idade": "423"
}

pessoa3 = {
    "nome": "Maria",
    "idade": "232"
}


pessoas = [pessoa1, pessoa2, pessoa3]

for pessoa in pessoas:
    print("Nome " +pessoa["nome"])
    print("Idade "+pessoa["idade"])

