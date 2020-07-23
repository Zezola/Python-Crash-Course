job = {}

# Setando a flag

flag = True

while flag:
    name = input("Whats your name: ")
    resposta = input("What is your dream job: ")
    job[name] = resposta
    repeat = input("Anyone else wants to answer?(yes or no)")
    if repeat == 'no':
        flag = False

print("---RESPOSTAS---")
print(vacation)
for nome, resposta in vacation.items():
    print(nome.title() + '\'s dream job is ' +resposta)