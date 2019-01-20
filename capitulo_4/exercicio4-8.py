# Escreva um programa que leia dois números e que pergunte qual operação 
# você deseja realizar. Você deve poder calcular a soma(+), subtração(-) 
# multiplicação(*) e divisão(/). Exiba o resultado da operação solicitada.

num_1 = int(input("Primeiro valor: "))
num_2 = int(input("Segundo valor: "))

ope = input("Escolha a operação (+ | - | * | /): ")

if ope == "+":
    print(num_1 + num_2)
elif ope == "-":
    print(num_1 - num_2)
elif ope == "*":
    print(num_1 * num_2)
elif ope == "/":
    print(num_1 / num_2)