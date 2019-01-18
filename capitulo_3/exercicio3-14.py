# Escreva um programa que pergunte a quantidade de km percorridos
# por um carro alugado pelo usuário, assim como a quantidade de dias
# pelos quais o carro foi alugado, Calcule o preço a pagar, sabendo
# que o carro custa R$ 60,00 por dia e R$ 0,15 por Km rodado.

dias = int(input("Dias de aluguel: "))
distacia = int(input("km percorridos: "))

preco_dia = float(dias * 60)
preco_distacia = float(distacia * 0.15)
total = preco_dia + preco_distacia

print("Valor a ser pago por dias de aluguel: %.2f" % preco_dia)
print("Valor a ser pago por km rodado: %.2f" % preco_distacia)
print("Total: R$ %.2f" % total )