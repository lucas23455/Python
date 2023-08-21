#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retanngulo,calcule e mostre o comprimento da hipotesusa

from math import hypot

co=float(input("digite o cateto oposto:"))

ca=float(input("digite o cateto adjacente:"))

hi= hypot(co,ca)

print("o valor da hipotenusa{:.2f}".format(hi))