# Código Resolução Vscode

# Entrada de dados
saldo_total = int(input("Digite o seu saldo: "))
valor_saque = int(input("Digite o valor de saque desejado: "))

# TODO: Criar as condições necessárias para impressão da saída, vide tabela de exemplos.

if saldo_total >= valor_saque:
    saldo = saldo_total - valor_saque
    print(f'Saque realizado com sucesso. Novo saldo: {saldo}')
else:
    print("Saldo insuficiente. Saque nao realizado")

# Código Resolução na Plataforma DIO

# Entrada de dados
saldo_total = int(input())
valor_saque = int(input())

# TODO: Criar as condições necessárias para impressão da saída, vide tabela de exemplos.

if saldo_total >= valor_saque:
    saldo = saldo_total - valor_saque
    print(f'Saque realizado com sucesso. Novo saldo: {saldo}')
else:
    print("Saldo insuficiente. Saque nao realizado!")


