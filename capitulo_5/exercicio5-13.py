# Escreva um programa que pergunte o valor inicial de uma dívida 
# e o juro mensal. Pergunte também o valor mensal que será 
# pago. Imprima o número de meses para que a dívida seja paga, 
# o total pago e o total de juros pago.

divida = int(input("Valor da dívida: ")) 
juro = int(input("Juro mensal: "))
pagamento_mensal_cliente = int(input("Pagamento mensal: "))

pagamento_mensal = pagamento_mensal_cliente - ((pagamento_mensal_cliente * juro) / 100)
meses = 1

while divida > 0:
    divida = divida - pagamento_mensal
    meses += 1

total_juros = juro * meses
total_pago = pagamento_mensal * meses
print("Paga em %d meses, %d de juros e %d no total pago!" % (meses, total_juros, total_pago))
