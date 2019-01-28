# O que acontece quando não verificamos se a lista 
# está vazia antes de chamarmos o método pop?
# IndexError: pop from empty list


lista = []

lista.pop()

print(lista)