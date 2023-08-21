#crie um algoritmo que leia um num e mostre o seu dobro,tiplo e raiz quadrada
import math
n=int(input("digite um num:"))

d=n*2
t=n*3
r=math.sqrt(n)

print("o dobro:{}".format(d))
print("o triplo:{}".format(t))
print("a raiz quadrada:{:.2f}".format(r))

