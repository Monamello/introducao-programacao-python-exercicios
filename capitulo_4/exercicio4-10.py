# Escreva um programa que calcule o preço a pagar pelo fornecimento 
# de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de intalação:
# R para residências, I para indústrias, e C para comércios. 
# Calcule o preço a pagar de acordo com a tabela.

faixa = int(input("Qual a quantidade de kWh consumida: "))
tipo = input("Qual o tipo de instalação? (R | I | C): ")

if tipo == 'R':
    if faixa > 500:
        print("Preço de 0.40")
    else:
        print("Preço de 0.65")

elif tipo == 'C':
    if faixa > 1000:
        print("Preço de 0.60")
    else:
        print("Preço de 0.55")

elif tipo == 'I':
    if faixa > 5000:
        print("Preço de 0.60")
    else:
        print("Preço de 0.55")
