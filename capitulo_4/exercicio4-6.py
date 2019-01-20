# Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. 
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens até 200 km, 
# e R$ 0,45 para viagens mais longas

distancia = int(input("Qual distância deseja percorrer? "))

if distancia <= 200:
    passagem = distancia * 0.50
    print("Passagem no valor de R$ %.2f" % passagem)
else:
    passagem = distancia * 0.45
    print("Passagem no valor de R$ %.2f" % passagem)