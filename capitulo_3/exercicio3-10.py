# Faça um programa que calcule o aumento de um salário.
# Ele deve solicitar o valor do salário e a porcentagem de aumento.
# Exiba o valor do aumento e do novo salário.

salario_atual = float(input("Salário atual: ")) 
porcentagem = float(input("Porcentagem de aumento: "))

reajuste = (salario_atual * porcentagem) / 100
salario_novo = reajuste + salario_atual

print("Reajuste: %.2f" % reajuste)
print("Novo salário: %.2f" % salario_novo)