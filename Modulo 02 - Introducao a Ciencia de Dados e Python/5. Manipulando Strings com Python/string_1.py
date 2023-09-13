
nome = "maTeus"

# Métodos para alteração da string Maiuscula, Minuscula e título
print(nome.upper())
print(nome.lower())
print(nome.title())

texto = " olá mundo!    "

# Métodos para alteração da string para eliminar espaços em branco
print(texto + ".")
print(texto.strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")

menu = "Python"

print("####" + menu + "####")
print(menu.center(14, "#"))
print("-".join(menu))
