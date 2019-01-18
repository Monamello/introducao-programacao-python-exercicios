# Escreva um programa para calcular a redução do tempo de vida de um fumante.
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
# Considere que um fumante perde 10 minutos de vida a cada cigarro,
# calcule quantos dias de vida um fumante perderá. Exiba o total em dias.

dia = int(input("Quantos cigarros você fuma por dia? "))
anos = int(input("Fuma a quantos anos? "))

um_ano = dia * 365
total_fumado = um_ano * anos 

min_fumados = total_fumado * 10

horas_fumados = min_fumados / 60

dias_fumando = horas_fumados / 24

print("Foram perdidos: %d dias de vida perdidos!" % dias_fumando)

