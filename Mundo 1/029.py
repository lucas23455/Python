#Escreva um programa que leia a velocidade de um carro
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. a multa vai custar R$ 7.00 por cada km acima do limite

v=int(input("digite a velocidade do seu carro:"))

if v >= 80:
    print ("voce foi multado!")
    total= (v-80)*7
    print("O valor da multa sera de {:.2f}".format(total)) 
else:
    print("Parabens, voce esta dentro do limite de velocidade")    