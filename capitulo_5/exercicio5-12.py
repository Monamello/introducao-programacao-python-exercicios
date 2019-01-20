# Altere o programa anterior de forma a perguntar 
# também o valor depositado mensalmente. Esse valor será 
# depositado no ínicio de cada mês, e você deve considerá-lo
# para o cálculo de juros do mês seguinte.

# deposito = float(input("Depósito inicial: "))
taxa = float(input("Taxa de juros: "))

meses = 0
renda_anual = 0

while meses < 10:
    deposito_mensal = float(input("Depósito para o mês: "))
    renda_mensal = (deposito_mensal * taxa) / 100
    renda_anual = renda_anual + renda_mensal
    meses = meses + 1
    print("Renda por mês(%d): %.2f" % (meses, renda_mensal))
print("Renda por 24 meses: %.2f" % renda_anual)