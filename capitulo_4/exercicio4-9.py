# Escreva um programa para aprovar um emprestimo bancário para compra de uma casa
# O programa deve perguntar o valor da casa, o salário e a quantidade de anos a pagar. 
# O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor 
# prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.

valor_casa = float(input("Valor da casa: ")) 
salario = float(input("Salário: "))
anos = float(input("Anos: "))

porcentagem_min = (30 * salario) / 100
n_parcelas = anos * 12
parcela = valor_casa / n_parcelas

if parcela > porcentagem_min:
    print("Valor das parcelas ultrapassa 30% do salário!")
else:
    print("A casa será paga em %d parcelas, no valor de %d" %(n_parcelas, parcela))



