# Escreva um programa que leia dois números. Imprima o 
# resultado da multiplicaçãodo primeiro pelo segundo.
# Utilize apenas os operadores de soma e subtração para calcular 
# o resultado. Lembre-se que podemos entender a multiplicação de 
# dois números como somas sucessivas de um deles. Assim, 4x5 = 5+5+5+5 = 4+4+4+4.

num_1 = int(input("Primeiro número: "))
num_2 = int(input("Segundo número: "))

x = 0
m = 0

while x < num_1:
    m = m + num_2
    x = x + 1
print(m)
