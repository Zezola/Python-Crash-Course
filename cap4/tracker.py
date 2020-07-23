saldoInicial = float(input("Digite o seu saldo\n"))
saldoAtual = saldoInicial

compras = []
continuarComprando = True

while (continuarComprando):
    compra = float(input("Preco do item: \n"))
    saldoAtual -= compra
    resposta = str(input("Continuar comprando?"))
    while (resposta.lower() == 's'):
        continuarComprando = True



