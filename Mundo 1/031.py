#Desenvolva um programa que pergunte a distancia de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por KM para viagens de até 200km e R$0,45 para viagens longas

d=float(input("qual a distancia percorrida pela viagem?"))

if d <=200:
    t=d*0.50
    print("O valor a pagar R${}".format(t))
else:
    t=d*0.45
    print("O valor a pagar será R${}".format(t))    