#faça um programa que leia um angulo qualquer e mostre na tela o valor de seno,cosseno e tangente desse angulo

from math import cos,sin,tan,radians


an=float(input("digite qualquer angulo que deseja:"))

seno=    sin(radians(an))
cosseno= cos(radians(an))
tangente=tan(radians(an))

print("o angulo de seno {}: {:.2f}".format(an,seno))
print("o angulo de cosseno {}: {:.2f}".format(an,cosseno))
print("o angulo de tangente {}: {:.2f}".format(an,tangente))


