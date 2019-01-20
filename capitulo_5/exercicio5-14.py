# Escreva um programa que leia números inteiros do teclado.
# O programa dele ler os números até que o usuário digite 0.
# No final da execução exiba a quantidade de números digitados,
# assim como a soma e a média arítmética.

soma = 0
c = 0

while True:
    n = int(input("Digite um número (0 para sair!): "))
    if n == 0:
        break
    else:
        soma = soma + n
        c += 1

media = soma / c

print("Soma = %d" % soma)
print("Média = %d" % media)

