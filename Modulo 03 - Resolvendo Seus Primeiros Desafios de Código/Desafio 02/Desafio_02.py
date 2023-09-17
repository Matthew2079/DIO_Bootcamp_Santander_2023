# Código Resolução Vscode

ativos = []

# Entrada da quantidade de ativos
quantidadeAtivos = int(input("Digite a quantidade de ativos: "))
print(quantidadeAtivos)

# Entrada dos códigos dos ativos
for quantidade in range(0,quantidadeAtivos,1):
    codigoAtivo = (input("Digite o nome do seu ativo: "))
    ativos.append(codigoAtivo)

# TODO: Ordenar os ativos em ordem alfabética.
ativos.sort()

# TODO: Imprimir a lista de ativos ordenada, conforme a tabela de exemplos.
for ativo in ativos:
    print(ativo)



# Código Resolução na Plataforma DIO
ativos = []

# Entrada da quantidade de ativos
quantidadeAtivos = int(input())

# Entrada dos códigos dos ativos
for quantidade in range(quantidadeAtivos):
    codigoAtivo = input()
    ativos.append(codigoAtivo)

# TODO: Ordenar os ativos em ordem alfabética.
ativos.sort()

# TODO: Imprimir a lista de ativos ordenada, conforme a tabela de exemplos.
for ativo in ativos:
    print(ativo)

