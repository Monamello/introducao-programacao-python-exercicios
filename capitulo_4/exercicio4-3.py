# Escreva um programa que leia três números e que imprima o maior e o menor

num_1 = int(input("Digite o primeiro número: "))
num_2 = int(input("Digite o segundo número: "))
num_3 = int(input("Digite o terceiro número: "))

if num_1 > num_2 and num_1 > num_3:
    print("%d é o maior!" % num_1)
elif num_2 > num_1 and num_2 > num_3:
    print("%d é o maior!" % num_2)
elif num_3 > num_1 and num_3 > num_2:
    print("%d é o maior!" % num_3)

if num_1 < num_2 and num_1 < num_3:
    print("%d é o menor!" % num_1)
elif num_2 < num_1 and num_2 < num_3:
    print("%d é o menor!" % num_2)
elif num_3 < num_1 and num_3 < num_2:
    print("%d é o menor!" % num_3)



       
