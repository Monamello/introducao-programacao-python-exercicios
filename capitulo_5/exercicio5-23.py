# Escreva um programa que leia um número e verifique se é ou não 
# número primo. Para fazer essa verificação, calcule o resto da divisão
# do número por 2 e depois por todos os números ímpares até o número lido.
# Se o resto de uma dessas divisões for igual a zero, o número primo que é par.

num = int(input("Digite um número: "))

resto = num % 2

x = 1
while num >= x:
    resto = num % x
    if resto == 0:
        print("não é primo!")
    x = x + 2