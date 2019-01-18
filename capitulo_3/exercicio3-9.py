# Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário
# Calcule o total em segundos.

dias = int(input("Dias: "))
horas = int(input("Horas: "))
minutos =  int(input("Minutos: "))
segundos = int(input("Segundos: "))


dias_seg = 86400 * dias
horas_seg = 3600 * horas
minutos_seg = 60 * minutos

total = dias_seg + horas_seg + minutos_seg + segundos

print("Total em segundo é: %d" % total)