# Escreva um programa que pergunte a velocidade do carro de um usuário. 
# Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. 
# Nesse caso exiba o valor da multa , cobrando por R$ 5 por km acima de 80 km/h.

v_usuario = int(input("Qual a velocidade do carro: "))
v_permitida = 80

if v_usuario > v_permitida:
    multa = (v_usuario - v_permitida) * 5
    print("Você foi multado no valor de R$ %d" % multa)
else:
    print("Parabéns, você está na velocidade permitida!")
