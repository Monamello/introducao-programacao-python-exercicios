# Modifique o programa anterior a ler um número n.
# Imprima os n primeiros números primos

num = int(input("Digite um número: "))

resto = num % 2

x = 1

while num > x:
    print(x)
    resto = num % x
    if resto == 0:
        print("é primo!")
    x = x + 1