#Faça um programa que leia 3 numeros e mostre qual é o maior e qual é o menor

n1=int(input("digite o 1°num:"))
n2=int(input("digite o 2°num:"))
n3=int(input("digite o 3°num:"))

menor=n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3

maior=n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3

print ("O MENOR numero digitado foi:", menor) 
print ("O MAIOR numero digitado foi:", maior )

  