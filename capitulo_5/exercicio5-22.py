# Escreva um programa que exiba uma lista de opções(menu):
# adição, subtração, divisão, multiplicação e sair. 
# Imprima a tabuada da operação escolhida. Repita até que a 
# opção saída seja escolhida.

# menu = "a = adição, s = subtração, d = divisão, m = multiplicação e s = sair"
# print(menu)
tabuada = input("Digite sua escolha: ") 

numero = 1
while opcao != 's':
    tabuada = int(input("Tabuada: "))
    if tabuada <= 10:
        numero +=1
        print("%d x %d = %d" % (tabuada, numero, tabuada * numero))
    
    if numero == 11:
        numero = 1
    tabuada +=1


# tabuada = 1

# while tabuada <= 10:
#     numero = 1
#     while