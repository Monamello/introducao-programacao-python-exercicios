# Faça um programa que solicite o preço de uma mercadoria e
# o percentual de desconto. Exiba o valor do desconto e o preço a pagar.

preco = float(input("Preço da mercadoria: "))
desconto = float(input("Desconto na mercadoria: "))

porcentagem_desconto = (preco * desconto) / 100
preco_final = preco - porcentagem_desconto

print("Preço final com desconto: ", preco_final)