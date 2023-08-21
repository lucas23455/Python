#Crie um programa que leia um numero inteiro e mostre na tela se ele é par ou impar

i=int(input("digite um numero:"))
if i%2==0:
    print("{} é PAR".format(i))
else:
    print("{} é IMPAR".format(i))