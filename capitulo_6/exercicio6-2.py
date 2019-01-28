# Faça um programa que leia duas listas e gere 
# uma terceira com das duas primeiras


lista_1 = [1, 2, 3]
lista_2 = ["a", "b", "c"]

tam = len(lista_1)
x = 0

while x < tam:
    pos = lista_1[x]
    lista_2.append(pos)
    x+=1
listao = lista_2
print(listao)
