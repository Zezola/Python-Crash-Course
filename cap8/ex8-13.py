def construir_perfil(nome, sobrenome, **info):
    #Fazer o dicionario vazio
    perfil = {}
    # Adicionar os valores que temos certeza que vao entrar no dicionario
    perfil['nome'] = nome
    perfil['sobrenome'] = sobrenome
    # Adicionar os argumentos arbitrários ao dicionario
    for chave, valor in info.items():
        perfil[chave] = valor
    # Retornar o perfil completo
    return perfil

perfil = construir_perfil("Jose", "Castro", cabelo = "castanho", altura = "161cm", idade = "24")

for item, valor in perfil.items():
    print(item + " = " + valor)