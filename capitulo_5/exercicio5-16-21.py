# Execute o programa da listagem 5.14 para 
# os seguintes valores: 501, 745, 384, 2, 7, e 1.
# OK!!!!!!

# O que acontece se digitarmos 0 no valor a pagar?
# OK !!!!!!- Retorna "0 cédulas de R$ 50"

# Modifique o programa para trabalhar também com notas de 100
# OK !!!!!!

# Modifique o programa para aceitar valores decimais, 
# ou seja, também também contar moedas de 0,01 0,02 0,05 
# 0,10 e 0,50.

# O que acontece se digitarmos 0.001 no programa anterior?
# Caso ele não funcione, altere-o de forma a corrigir o problema 

# Reescreva o programa da listagem 5.14 de forma a continuar executando
#  até que o valor digitado seja 0. Utilize repetições aninhadas.


valor = float(input("Digite o valor a pagar: "))
cedulas = 0
atual = 100.00
apagar = valor

while True:
    if atual <= apagar:
        apagar -= atual
        cedulas += 1
    else:
        print("%d cédulas de R$ %.2f" % (cedulas, atual))

        if apagar == 0:
            break

        if atual == 100.00:
            atual = 50.00
                
        elif atual == 50.00:
            atual = 20.00

        elif atual == 20.00:
            atual = 10.00

        elif atual == 10.00:
            atual = 5.00

        elif atual == 5.00:
            atual = 1.00

        elif atual == 1.00:
            atual = 0.50

        elif atual == 0.50:
            atual = 0.10

        elif atual == 0.10:
            atual = 0.05

        elif atual == 0.05:
            atual = 0.02

        elif atual == 0.02:
            atual = 0.01

        cedulas = 0
            