#desenvolva uma logica que leia peso e altura de uma pessoa, calcule seu imc e mostre seu status de acordo com a tabela abaixo:

peso=float(input("qual é seu peso?"))
altura=float(input("qual é sua altura?"))

imc=peso/(altura**2)

if imc < 18.5:
    print("abaixo do peso")
elif imc >= 18.5 and imc < 25:
    print ("Peso ideal ")
elif imc <= 25 and imc < 30:
    print("sobrepeso")
elif imc <=30 and imc <40:
    print("obesidade morbida") 
else:
    print("cuidado")       
