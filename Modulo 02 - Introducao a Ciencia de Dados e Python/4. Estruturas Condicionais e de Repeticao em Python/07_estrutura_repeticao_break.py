

while True:
     numero = int(input("Informe um número: "))

     if numero == 10:
         break # para execução

     print(numero)

for numero in range(100):

    if numero % 2 == 0:
        continue # procede executando
    
    print(numero, end=" ")