#Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuario se elas podem ou nao formar um triangulo

r1=float(input("digite a 1°reta:"))
r2=float(input("digite a 2°reta:"))
r3=float(input("digite a 3°reta:"))

if r1< r2 +r3 and r2<r1+r3 and r3<r1+r2:
    print ("é possivel formar um triangulo")
else :
    print ("não é possível formar um triângulo.")

