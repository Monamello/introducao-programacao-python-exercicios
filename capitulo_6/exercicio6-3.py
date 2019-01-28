# Faça um programa que percorra duas listas e 
# gere uma terceira sem elementos repetidos

lista_1 = [1, 2, 3]
lista_2 = ["a", "b", "c", 1, 2,]

tam = len(lista_1)
x = 0

while x < tam:
    pos = lista_1[x]
    if not pos in lista_2:
        lista_2.append(pos)
    x+=1
listao = lista_2
print(listao)