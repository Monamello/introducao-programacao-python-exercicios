# Escreva um programa que leia dois números. Imprima a divisão 
# inteira do primeiro pelo segundo, assim como o resto da divisão. 
# Utilize apenas os operadores de soma e subtração para calcular o resultado. 
# Lembre-se de que podemos entender o quociente da divisão de dois números 
# como a quantidade de vezes que podemos retirar o divisor dividendo. 
# Logo , 20 / 4 = 5, uma vez que podemos subtrair cinco vezes de 20.

num_1 = int(input("Primeiro número: "))
num_2 = int(input("Segundo número: "))

x = 0

while num_1 != 0:
    num_1 = num_1 - num_2
    x = x + 1
    if num_1 < num_2 and num_1 > 0:
        print("Divisão: %d  | Resto: %d" % (x, num_1))
        break

print("Divisão: %d" % x)
