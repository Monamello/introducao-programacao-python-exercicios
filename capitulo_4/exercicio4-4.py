# Escreva um programa que pergunte o salário do funcionário 
# e calcule o valor do aumento. Para salários superiores a R$ 1.250,00, 
# calcule o aumento de 10%. Para os inferiores ou iguais, 15%.

salario = int(input("Salário: "))
media = 1250

if salario > media:
    extra = (salario * 10) / 100
    novo_salario = extra + salario
    print("Novo salário de R$ %d" % novo_salario)
else:
    extra =  (salario * 15) / 100
    novo_salario = extra + salario
    print("Novo salário de R$ %d" % novo_salario)