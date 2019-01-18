# Escreva uma expressão que será utilizada para decidir se uma aluna foi ou não aprovada.
# Para ser aprovada, todas as médias da aluna devem ser maiores que 7. 
# Considere que a aluna cursa apenas três matérias, 
# e que a nota de cada uma está armazenada nas seguintes variáveis: materia1, materia2 e materia3.

materia1 = int(input("Nota da matéria 1: "))
materia2 = int(input("Nota da matéria 2: "))
materia3 = int(input("Nota da matéria 3: "))

materias = materia1 + materia2 + materia3

media = materias / 3

if media >= 7:
    print("Aprovada, média %d" % media)
else:
    print("Reprovada, média %d" % media)