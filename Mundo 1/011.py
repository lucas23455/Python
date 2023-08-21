#faça um programa que leia a altura e largura de uma parede em metros, calcule sua area e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta, pinta uma area de 2m2

h=float(input("altura da parede:"))
l=float(input("largura da parede:"))

a=l*h
t=a/2

print("A area da parede {} metros".format(a))
print("serão necessario {} de tinta para pintar a parede".format(t))
