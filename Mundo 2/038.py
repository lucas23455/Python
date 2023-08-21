#escreva um programa que leia dois num inteiros e compare-os, mostrando na tela uma mensagem

n1=int(input("digite o 1°valor:"))
n2=int(input("Digite o 2ºvalor:"))

if n1>n2:
    print("O primeiro valor é maior")
elif n2>n1:
    print("O segundo valor é maior")
else:
    print("Os dois valores são iguais")        