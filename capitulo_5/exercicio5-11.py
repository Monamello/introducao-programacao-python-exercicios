# Escreva um programa que pergunte o depósito inicial
# e a taxa de juros de uma poupança. Exiba os valores mês 
# a mês para os 24 primeiros meses. Escreva o total ganho 
# com juros no período.

deposito = float(input("Depósito inicial: "))
taxa = float(input("Taxa de juros: "))

meses = 0
renda_anual = 0

while meses < 24:
    renda_mensal = (deposito * taxa) / 100
    renda_anual = renda_anual + renda_mensal
    meses = meses + 1
    print("Renda por mês(%d): %.2f" % (meses, renda_mensal))
print("Renda por 24 meses: %.2f" % renda_anual)