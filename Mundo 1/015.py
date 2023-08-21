#Escreva um programa que pergunte a quantidade de KM percorrindos por um carro alugado e a quantidade de dias pelos quais foi alugado. calcule o preço a pagar, sabendo que o carro custa R$60 e R$0.15 por KM rodado

quant=float(input("qual foi a quantidade de KM percorrindo pelo carro?"))
dias=int(input("quantos dias voce usou o carro?"))

tolcar=quant*0.15
total=dias*60+tolcar

print("o valor total do custos do carro sera R${}".format(total))