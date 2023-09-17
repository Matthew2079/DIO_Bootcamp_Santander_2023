# Código Resolução Vscode

valor_inicial = float(input("Digite seu valor de investimento: "))
taxa_juros = float(input("Digite sua taxa de juros ao mês: "))
periodo = (input("Digite o período em anos: "))

valor_final = valor_inicial

# TODO: Iterar, baseado no período em anos, para calculo do valorFinal com os juros.

for tempo in periodo:
     valor_final = valor_final * (1 + taxa_juros)

print("Valor final do investimento: R$", round(valor_final, 2))

# Código Resolução na Plataforma DIO

valor_inicial = float(input())
taxa_juros = float(input())
periodo = int(input())

valor_final = valor_inicial

# TODO: Iterar, baseado no período em anos, para calculo do valorFinal com os juros.

for tempo in range(periodo):
    valor_final = valor_final * (1 + taxa_juros)
    
print("Valor final do investimento: R$", round(valor_final, 2))



