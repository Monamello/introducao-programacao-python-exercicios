# Escreva um programa que exiba uma lista de opções(menu):
# adição, subtração, divisão, multiplicação e sair. 
# Imprima a tabuada da operação escolhida. Repita até que a 
# opção saída seja escolhida.

# print(menu)
menu = ''
print(menu)
while menu != 's':
    menu = input("+ = adição, - = subtração, / = divisão, * = multiplicação e s = sair: ")
    if menu == 's':
        break

    x = 1
    n = int(input("Tabuada de: "))
    while x <= 10:
        if menu == '+':
            resultado = n+x
            print("%d + %d = %d" %(n, x, resultado))

        elif menu == '-':
            resultado = n-x
            print("%d - %d = %d" %(n, x, resultado))

        elif menu == '/':
            resultado = n/x
            print("%d / %d = %d" %(n, x, resultado))

        elif menu == '*':
            resultado = n*x
            print("%d x %d = %d" %(n, x, resultado))

        x=x+1