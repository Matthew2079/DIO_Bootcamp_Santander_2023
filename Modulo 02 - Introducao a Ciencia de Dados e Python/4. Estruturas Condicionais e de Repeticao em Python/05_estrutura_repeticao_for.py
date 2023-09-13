
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

# Exemplo iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()
    print("Executa final do laço")

# Exemplo função built-in range
for numero in range(0, 51, 5):
    print(numero, end="")