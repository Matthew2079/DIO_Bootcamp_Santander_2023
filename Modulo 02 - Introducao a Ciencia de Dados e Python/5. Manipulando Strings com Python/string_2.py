
# Interpolação de variáveis

nome = "Mateus"
idade = 28
profissao = "Progamador"
linguagem = "Python"

dados = {"nome": "Mateus", "idade": 28}
saldo = 45.435

print("Nome: %s Idade: %d" % (nome,idade)) #old style% - Não utilizado 

# Modo .format
print("Nome: {} Idade: {}" .format(nome,idade)) 
print("Nome: {1} Idade: {0}" .format(nome,idade)) 
print("Nome: {1} Idade: {0} Nome: {1} {1}" .format(nome,idade)) 
print("Nome: {nome} Idade: {idade}" .format(nome=nome, idade=idade)) 
print("Nome: {name} Idade: {age}" .format(age=idade, name=nome)) 
print("Nome: {nome} Idade: {idade}" .format(**dados)) 

# Modo f String - Mais Usado
print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")



