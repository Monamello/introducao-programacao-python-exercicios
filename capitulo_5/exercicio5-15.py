# Escreva um programa para controlar uma pequena máquina 
# resgistradora. Você deve solicitar ao usuário que digite 
# o código do produto e a quantidade comprada. Utilize a 
# tabela abaixo para obter o preço de cada produto.

soma = 0
cod = 1
while cod !=0:
    cod = int(input("Código do produto: "))
    quant = int(input("Quantidade do produto: "))
    if cod == 1:
        valor = 0.50 * quant
        soma = soma + valor
    elif cod == 2:
        valor = 1.00 * quant
        soma = soma + valor
    elif cod == 3:
        valor = 4.00 * quant
        soma = soma + valor
    elif cod == 5:
        valor = 7.00 * quant 
        soma = soma + valor
    elif cod == 9:
        valor = 8.00 * quant
        soma = soma + valor
    else:
        print("Código %d inválido!" % cod)

print("Valor a ser pago: %.2f " % soma)