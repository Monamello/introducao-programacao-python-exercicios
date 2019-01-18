# Escreva um programa que calcule o tempo de viagem de carro.
# Pergunte a distância a percorrer e a velocidade média para a viagem.

distancia = int(input("Distância percorrida na viagem(km): "))
velocidade = int(input("Velocidade média na viagem(km/h): "))

tempo = distancia / velocidade

print("Tempo de viagem: %d horas!" % tempo)