# Modifique o programa anterior para imprimir de 1 até o número 
# digitando pelo usuário, mas, dessa vez, apenas número ímpares.

fim = int(input("Fim: "))

x = 1

while x <= fim:
    if x % 2 == 1:
        print(x)
    x = x + 1