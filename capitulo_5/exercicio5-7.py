# Modifique o programa anterior de forma que o usuário também 
# digite o ínicio e o fim da tabuada em vez de começar com 1 e 10.

n = int(input("Tabuada de: "))
inicio = int(input("Inicio: "))
fim = int(input("Fim: "))

while inicio <= fim :
    resultado = n*inicio
    print("%d x %d = %d" %(n, inicio, resultado))
    inicio=inicio+1