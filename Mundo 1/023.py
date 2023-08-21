#faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados

num=int(input("digite um num inteiro:"))
u = num //1 % 10 #pega o unidade do número dividindo
d = num //10% 10 # pega a dezena do número div
c = num//100 % 10 # pega a centena do número div
m = num//1000 % 10 # pega a milhar do número
print ("unidade:", u)
print ("dezena:", d )
print ("centena", c)
print ("milhar:", m)


